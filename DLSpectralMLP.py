from __future__ import annotations

from typing import Any, Dict, List, Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class DLSpectralMLP(nn.Module):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self.config = dict(config)

        d_in = int(config["d_in"])
        hidden: List[int] = [int(x) for x in config["hidden"]]
        p = float(config.get("dropout", 0.0))
        use_ln = bool(config.get("layer_norm", True))
        use_sn = bool(config.get("spectral_norm", True))
        act_name = str(config.get("activation", "gelu")).lower()

        def act() -> nn.Module:
            if act_name == "relu":
                return nn.ReLU()
            if act_name == "tanh":
                return nn.Tanh()
            return nn.GELU()

        def linear(a: int, b: int) -> nn.Module:
            layer = nn.Linear(a, b)
            return nn.utils.spectral_norm(layer) if use_sn else layer

        layers: List[nn.Module] = []
        if use_ln:
            layers.append(nn.LayerNorm(d_in))

        in_dim = d_in
        for h in hidden:
            layers.append(linear(in_dim, h))
            layers.append(act())
            if p > 0:
                layers.append(nn.Dropout(p))
            in_dim = h

        layers.append(linear(in_dim, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        s = self.net(z).squeeze(-1)
        return s

    def loss(self, logits: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return F.binary_cross_entropy_with_logits(logits, y.float())
