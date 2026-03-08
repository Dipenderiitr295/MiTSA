from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class GradientReversalFn(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x: torch.Tensor, lambd: torch.Tensor) -> torch.Tensor:
        ctx.save_for_backward(lambd)
        return x

    @staticmethod
    def backward(ctx, grad_output: torch.Tensor):
        (lambd,) = ctx.saved_tensors
        return -lambd * grad_output, None


class GradientReversal(nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, x: torch.Tensor, lambd: torch.Tensor) -> torch.Tensor:
        return GradientReversalFn.apply(x, lambd)


class ValueMLP(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        d = int(config["d_model"])
        hidden = list(config["value_mlp_hidden"])
        p = float(config.get("dropout", 0.0))
        layers = []
        in_dim = 1
        for h in hidden:
            layers.append(nn.Linear(in_dim, int(h)))
            layers.append(nn.GELU())
            if p > 0:
                layers.append(nn.Dropout(p))
            in_dim = int(h)
        layers.append(nn.Linear(in_dim, d))
        self.net = nn.Sequential(*layers)

    def forward(self, v: torch.Tensor) -> torch.Tensor:
        if v.dim() == 1:
            v = v.unsqueeze(-1)
        return self.net(v)


class AttentionPooling(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        d = int(config["d_model"])
        self.q = nn.Parameter(torch.empty(d))
        nn.init.normal_(self.q, mean=0.0, std=0.02)

    def forward(self, h: torch.Tensor, mask: Optional[torch.Tensor]) -> torch.Tensor:
        scores = torch.einsum("btd,d->bt", h, self.q)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, torch.finfo(scores.dtype).min)
        w = torch.softmax(scores, dim=-1)
        z = torch.einsum("bt,btd->bd", w, h)
        return z


class MiTSAEncoder(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self.config = dict(config)
        d = int(config["d_model"])
        vocab_size = int(config["vocab_size_total"])
        self.name_emb = nn.Embedding(vocab_size, d)
        self.value_emb = ValueMLP(config)

        enc_layer = nn.TransformerEncoderLayer(
            d_model=d,
            nhead=int(config["n_heads"]),
            dim_feedforward=int(config["ffn_dim"]),
            dropout=float(config.get("dropout", 0.0)),
            activation=str(config.get("activation", "gelu")),
            batch_first=True,
            norm_first=bool(config.get("norm_first", True)),
        )
        self.encoder = nn.TransformerEncoder(enc_layer, num_layers=int(config["n_layers"]))
        self.pool = AttentionPooling(config)

    def forward(
        self,
        name_ids: torch.Tensor,
        values: torch.Tensor,
        pad_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        e_name = self.name_emb(name_ids)
        e_val = self.value_emb(values)
        t = e_name + e_val
        key_padding_mask = None
        if pad_mask is not None:
            key_padding_mask = (pad_mask == 0)
        h = self.encoder(t, src_key_padding_mask=key_padding_mask)
        z = self.pool(h, pad_mask)
        return z


class MiTSAHeads(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        d = int(config["d_model"])
        n_domains = int(config["n_domains"])
        hidden = list(config["head_hidden"])
        p = float(config.get("dropout", 0.0))

        def make_mlp(out_dim: int) -> nn.Sequential:
            layers = []
            in_dim = d
            for h in hidden:
                layers.append(nn.Linear(in_dim, int(h)))
                layers.append(nn.GELU())
                if p > 0:
                    layers.append(nn.Dropout(p))
                in_dim = int(h)
            layers.append(nn.Linear(in_dim, out_dim))
            return nn.Sequential(*layers)

        self.defect_head = make_mlp(1)
        self.domain_head = make_mlp(n_domains)
        self.grl = GradientReversal()

    def forward(
        self,
        z: torch.Tensor,
        grl_lambda: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        defect_logits = self.defect_head(z).squeeze(-1)
        z_grl = self.grl(z, grl_lambda)
        domain_logits = self.domain_head(z_grl)
        return defect_logits, domain_logits


class MiTSA(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self.encoder = MiTSAEncoder(config)
        self.heads = MiTSAHeads(config)

    def forward(
        self,
        name_ids: torch.Tensor,
        values: torch.Tensor,
        pad_mask: Optional[torch.Tensor],
        grl_lambda: torch.Tensor,
    ) -> Dict[str, torch.Tensor]:
        z = self.encoder(name_ids, values, pad_mask)
        defect_logits, domain_logits = self.heads(z, grl_lambda)
        return {"z": z, "defect_logits": defect_logits, "domain_logits": domain_logits}

    def losses(
        self,
        outputs: Dict[str, torch.Tensor],
        y_defect: torch.Tensor,
        y_domain: torch.Tensor,
        alpha: torch.Tensor,
    ) -> Dict[str, torch.Tensor]:
        defect_logits = outputs["defect_logits"]
        domain_logits = outputs["domain_logits"]
        loss_defect = F.binary_cross_entropy_with_logits(defect_logits, y_defect.float())
        loss_domain = F.cross_entropy(domain_logits, y_domain.long())
        loss_total = loss_defect + alpha * loss_domain
        return {"loss_total": loss_total, "loss_defect": loss_defect, "loss_domain": loss_domain}
