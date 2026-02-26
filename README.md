# MiTSA
# Details of Datsets
1. **AEEEM:** M. D’Ambros, M. Lanza, and R. Robbes, “Evaluating defect prediction approaches: a benchmark and an extensive comparison,” Empirical Software Engineering, vol. 17, pp. 531–577, 2012.
2. **JIRA:** S. Yatish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn, “Mining software defects: Should we consider affected releases?” in 2019 IEEE/ACM 41st international conference on software engineering (ICSE). IEEE, 2019, pp. 654–665.
3. **PROMISE:** T. Menzies, R. Krishna, and D. Pryor, “The promise repository of empirical software engineering data (2015),” URL http://promisedata.googlecode. com, 2015.
4. **SOFTLAB:** B. Turhan, T. Menzies, A. B. Bener, and J. Di Stefano, “On the relative value of cross-company and within-company data for defect prediction,” Empirical Software Engineering, vol. 14, no. 5, pp. 540–578, 2009.

# Metrics Details of AEEEM Dataset
| **Abbreviation**                   | **Description**                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| ck\_oo\_wmc                        | Weighted method count                                                              |
| ck\_oo\_dit                        | Depth of inheritance tree                                                          |
| ck\_oo\_rfc                        | Response for class                                                                 |
| ck\_oo\_noc                        | Number of children                                                                 |
| ck\_oo\_cbo                        | Coupling between objects                                                           |
| ck\_oo\_lcom                       | Lack of cohesion in methods                                                        |
| ck\_oo\_fanin                      | Number of other classes that reference the class                                   |
| ck\_oo\_fanout                     | Number of other classes referenced by the class                                    |
| ck\_oo\_noa                        | Number of attributes                                                               |
| ck\_oo\_nopa                       | Number of public attributes                                                        |
| ck\_oo\_nopra                      | Number of private attributes                                                       |
| ck\_oo\_noai                       | Number of attributes inherited                                                     |
| ck\_oo\_loc                        | Number of lines of code                                                            |
| ck\_oo\_nom                        | Number of methods                                                                  |
| ck\_oo\_nopm                       | Number of public methods                                                           |
| ck\_oo\_noprm                      | Number of private methods                                                          |
| ck\_oo\_nomt                       | Number of methods inherited                                                        |
| WCHU\_wmc                          | Weighted churn of weighted method count                                            |
| WCHU\_dit                          | Weighted churn of depth of inheritance tree                                        |
| WCHU\_rfc                          | Weighted churn of response for class                                               |
| WCHU\_noc                          | Weighted churn of number of children                                               |
| WCHU\_cbo                          | Weighted churn of coupling between objects                                         |
| WCHU\_lcom                         | Weighted churn of lack of cohesion in methods                                      |
| WCHU\_fanin                        | Weighted churn of number of other classes that reference the class                 |
| WCHU\_fanout                       | Weighted churn of number of other classes referenced by the class                  |
| WCHU\_noa                          | Weighted churn of number of attributes                                             |
| WCHU\_nopa                         | Weighted churn of number of public attributes                                      |
| WCHU\_nopra                        | Weighted churn of number of private attributes                                     |
| WCHU\_noai                         | Weighted churn of number of attributes inherited                                   |
| WCHU\_loc                          | Weighted churn of number of lines of code                                          |
| WCHU\_nom                          | Weighted churn of number of methods                                                |
| WCHU\_nopm                         | Weighted churn of number of public methods                                         |
| WCHU\_noprm                        | Weighted churn of number of private methods                                        |
| WCHU\_nomt                         | Weighted churn of number of methods inherited                                      |
| LDHH\_wmc                          | Linear decayed history entropy of weighted method count                            |
| LDHH\_dit                          | Linear decayed history entropy of depth of inheritance tree                        |
| LDHH\_rfc                          | Linear decayed history entropy of response for class                               |
| LDHH\_noc                          | Linear decayed history entropy of number of children                               |
| LDHH\_cbo                          | Linear decayed history entropy of coupling between objects                         |
| LDHH\_lcom                         | Linear decayed history entropy of lack of cohesion in methods                      |
| LDHH\_fanin                        | Linear decayed history entropy of number of other classes that reference the class |
| LDHH\_fanout                       | Linear decayed history entropy of number of other classes referenced by the class  |
| LDHH\_noa                          | Linear decayed history entropy of number of attributes                             |
| LDHH\_nopa                         | Linear decayed history entropy of number of public attributes                      |
| LDHH\_nopra                        | Linear decayed history entropy of number of private attributes                     |
| LDHH\_noai                         | Linear decayed history entropy of number of attributes inherited                   |
| LDHH\_loc                          | Linear decayed history entropy of number of lines of code                          |
| LDHH\_nom                          | Linear decayed history entropy of number of methods                                |
| LDHH\_nopm                         | Linear decayed history entropy of number of public methods                         |
| LDHH\_noprm                        | Linear decayed history entropy of number of private methods                        |
| LDHH\_nomt                         | Linear decayed history entropy of number of methods inherited                      |
| CvsEntropy                         | Entropy of CVS change log                                                          |
| CvsWEntropy                        | Weighted Entropy of CVS change log                                                 |
| CvsLogEntropy                      | Logarithmic Entropy of CVS change log                                              |
| CvsExpEntropy                      | Exponential Entropy of CVS change log                                              |
| CvsLinEntropy                      | Linear Entropy of CVS change log                                                   |
| numberOfNonTrivialBugsFoundUntil   | Number of non-trivial bugs found until the corresponding fix                       |
| numberOfCriticalBugsFoundUntil     | Number of critical bugs found until the corresponding fix                          |
| numberOfHighPriorityBugsFoundUntil | Number of high priority bugs found until the corresponding fix                     |
| numberOfMajorBugsFoundUntil        | Number of major bugs found until the corresponding fix                             |
| numberOfBugsFoundUntil             | Number of bugs found until the corresponding fix                                   |

# Metrics Details of JIRA Dataset
| **Abbreviation**          | **Description**                                                            |
| ------------------------- | -------------------------------------------------------------------------- |
| AvgCyclomatic             | Average cyclomatic complexity for all nested functions or methods          |
| SumCyclomatic             | Sum of cyclomatic complexity of all nested functions or methods            |
| AvgCyclomaticModified     | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified     | Sum of modified cyclomatic complexity of all nested functions              |
| AvgCyclomaticStrict       | Average strict cyclomatic complexity for all nested functions or methods   |
| SumCyclomaticStrict       | Sum of strict cyclomatic complexity of all nested functions or methods     |
| AvgEssential              | Average essential complexity for all nested functions or methods           |
| SumEssential              | Sum of essential complexity of all nested functions or methods             |
| AvgLine                   | Average number of lines for all nested functions or methods                |
| AvgLineBlank              | Average number of blank lines for all nested functions or methods          |
| AvgLineCode               | Average number of lines containing source code for all nested functions    |
| AvgLineComment            | Average number of comment lines for all nested functions or methods        |
| CountClassBase            | Number of immediate base classes                                           |
| CountClassCoupled         | Number of other classes coupled to                                         |
| CountClassDerived         | Number of immediate subclasses                                             |
| MaxInheritanceTree        | Maximum depth of class in inheritance tree                                 |
| PercentLackOfCohesion     | 100% minus the average cohesion for package entities                       |
| CountDeclClass            | Number of classes                                                          |
| CountDeclClassMethod      | Number of class methods                                                    |
| CountDeclClassVariable    | Number of class variables                                                  |
| CountDeclFunction         | Number of functions                                                        |
| CountDeclInstanceMethod   | Number of instance methods                                                 |
| CountDeclInstanceVariable | Number of instance variables                                               |
| CountDeclMethod           | Number of local (non-inherited) methods                                    |
| CountDeclMethodDefault    | Number of local default methods                                            |
| CountDeclMethodPrivate    | Number of local (non-inherited) private methods                            |
| CountDeclMethodProtected  | Number of local protected methods                                          |
| CountDeclMethodPublic     | Number of local (non-inherited) public methods                             |
| CountLine                 | Number of physical lines                                                   |
| CountLineBlank            | Number of blank lines                                                      |
| CountLineCode             | Number of lines containing source code                                     |
| CountLineCodeDecl         | Number of lines containing declarative source code                         |
| CountLineCodeExe          | Number of lines containing executable source code                          |
| CountLineComment          | Number of lines containing comment                                         |
| CountSemicolon            | Number of semicolons                                                       |
| CountStmt                 | Number of statements                                                       |
| CountStmtDecl             | Number of declarative statements                                           |
| CountStmtExe              | Number of executable statements                                            |
| MaxCyclomatic             | Maximum cyclomatic complexity of all nested functions or methods           |
| MaxCyclomaticModified     | Maximum modified cyclomatic complexity of nested functions or methods      |
| MaxCyclomaticStrict       | Maximum strict cyclomatic complexity of nested functions or methods        |
| RatioCommentToCode        | Ratio of comment lines to code lines                                       |
| CountInput\_Min           | Min number of calling subprograms plus global variables read               |
| CountInput\_Mean          | Mean number of calling subprograms plus global variables read              |
| CountInput\_Max           | Max number of calling subprograms plus global variables read               |
| CountOutput\_Min          | Min number of called subprograms plus global variables set                 |
| CountOutput\_Mean         | Mean number of called subprograms plus global variables set                |
| CountOutput\_Max          | Max number of called subprograms plus global variables set                 |
| CountPath\_Min            | Min number of unique paths through a body of code                          |
| CountPath\_Mean           | Mean number of unique paths through a body of code                         |
| CountPath\_Max            | Max number of unique paths through a body of code                          |
| MaxNesting\_Min           | Min of maximum nesting level of control constructs in the function         |
| MaxNesting\_Mean          | Mean of maximum nesting level of control constructs in the function        |
| MaxNesting\_Max           | Max of maximum nesting level of control constructs in the function         |
| COMM                      | Number of Git commits                                                      |
| ADDED\_LINES              | Normalized number of lines added to the module                             |
| DEL\_LINES                | Normalized number of lines deleted from the module                         |
| ADEV                      | Number of active developers                                                |
| DDEV                      | Number of distinct developers                                              |
| MINOR\_COMMIT             | Developers contributing <5% of total code changes                          |
| MINOR\_LINE               | Developers contributing <5% of total LOC                                   |
| MAJOR\_COMMIT             | Developers contributing >5% of total code changes                          |
| MAJOR\_LINES              | Developers contributing >5% of total LOC                                   |
| OWN\_COMMIT               | Proportion of code changes by top contributor                              |
| OWN\_LINE                 | Proportion of lines of code by top contributor                             |

# Metrics Details of PROMISE Dataset
| **Abbreviation** | **Description** |
|------------------|-----------------|
| WMC              | Weighted Methods per Class |
| DIT              | Depth of Inheritance Tree |
| NOC              | Number of Children |
| CBO              | Coupling Between Object Classes |
| RFC              | Response for a Class |
| LCOM             | Lack of Cohesion in Methods |
| CA               | Afferent Couplings |
| CE               | Efferent Couplings |
| NPM              | Number of Public Methods |
| LCOM3            | Lack of Cohesion in Methods (variant of LCOM) |
| LOC              | Lines of Code |
| DAM              | Data Access Metric |
| MOA              | Measure of Aggregation |
| MFA              | Measure of Functional Abstraction |
| CAM              | Cohesion Among Methods of a Class |
| IC               | Inheritance Coupling |
| CBM              | Coupling Between Methods |
| AMC              | Average Method Complexity |
| CC               | McCabe’s Cyclomatic Complexity |
| MAX_CC           | Maximum Value of CC Among Methods in the Class |
| AVG_CC           | Average (Arithmetic Mean) CC of Methods in the Class |


# Metrics Details of SOFTLAB Dataset
| **Abbreviation**                     | **Description**                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| total_loc                        | Total number of physical lines of code (including blank and comment lines)                                                                             |
| blank_loc                        | Number of blank (empty) lines                                                                                                                          |
| comment_loc                      | Number of lines containing comments                                                                                                                    |
| code_and_comment_loc             | Number of lines containing both code and comment (inline comments)                                                                                     |
| executable_loc                   | Number of lines containing executable source code                                                                                                      |
| unique_operands                  | Number of distinct operands used in the module (Halstead n₂)                                                                                           |
| unique_operators                 | Number of distinct operators used in the module (Halstead n₁)                                                                                          |
| total_operands                   | Total occurrences of operands in the module (Halstead N₂)                                                                                              |
| total_operators                  | Total occurrences of operators in the module (Halstead N₁)                                                                                             |
| halstead_vocabulary              | Halstead vocabulary: total distinct tokens = unique_operators + unique_operands (n = n₁ + n₂)                                                          |
| halstead_length                  | Halstead length: total token occurrences = total_operators + total_operands (N = N₁ + N₂)                                                              |
| halstead_volume                  | Halstead volume: information content, typically ( V = N \cdot \log_2(n) )                                                                              |
| halstead_level                   | Halstead level: inverse of difficulty, typically ( L = 1/D ) (also described as implementation level)                                                  |
| halstead_difficulty              | Halstead difficulty: implementation difficulty, typically ( D = (n_1/2) \cdot (N_2/n_2) )                                                              |
| halstead_effort                  | Halstead effort: mental effort, typically ( E = D \cdot V )                                                                                            |
| halstead_error                   | Halstead estimated defects (error): typically ( B \approx V/3000 ) (variant-dependent)                                                                 |
| halstead_time                    | Halstead time to program: typically ( T = E/18 ) seconds (variant-dependent constant)                                                                  |
| branch_count                     | Number of branch points in the control-flow graph (e.g., conditional/loop branches)                                                                    |
| decision_count                   | Number of decision points (control predicates such as if/while/for/switch cases, depending on parser definition)                                       |
| call_pairs                       | Number of caller–callee pairs (function/procedure call relations), a proxy for inter-procedural complexity                                             |
| condition_count                  | Number of atomic Boolean conditions appearing in decision predicates                                                                                   |
| multiple_condition_count         | Number of compound/multiple-condition predicates (e.g., use of AND/OR chaining), proxy for logical complexity                                          |
| cyclomatic_complexity            | McCabe cyclomatic complexity ( V(G) ): number of linearly independent paths through the control-flow graph                                             |
| cyclomatic_density               | Cyclomatic complexity normalized by size (commonly ( V(G)/\text{LOC} ) or similar)                                                                     |
| decision_density                 | Decision points normalized by size (commonly decision_count/LOC or similar)                                                                            |
| design_complexity                | Design (structural) complexity reflecting call/branch structure at the design level (tool-specific definition; often related to module call structure) |
| design_density                   | Design complexity normalized by size (design_complexity per LOC or similar)                                                                            |
| normalized_cyclomatic_complexity | Cyclomatic complexity normalized/scaled (tool-specific; often adjusts for module size or minimum complexity baseline)                                  |
| formal_parameters                | Number of formal parameters in the function/procedure/module interface (proxy for interface complexity)                                                |



## F1-Score Comparison of the Proposed MiTSA Method Against HDP Baseline Methods

The table below presents the F1-score comparison of the proposed **MiTSA** approach against  state-of-the-art HDP baseline methods.

| Target Project     | MiTSA | FD-HDP | JIFA | MNAFM | BMEL+AMR | MHCPDP |
|-------------------|-------|--------|------|--------|----------|--------|
| Equinox           | 0.56  | 0.60   | 0.62 | 0.28   | 0.54     | 0.56   |
| Jdt               | 0.37  | 0.28   | 0.27 | 0.28   | 0.38     | 0.37   |
| Lucene            | 0.34  | 0.15   | 0.16 | 0.19   | 0.22     | 0.28   |
| Mylyn             | 0.25  | 0.49   | 0.47 | 0.21   | 0.20     | 0.22   |
| Pde               | 0.30  | 0.16   | 0.15 | 0.26   | 0.25     | 0.15   |
| Activemq-5.2.0    | 0.24  | 0.12   | 0.13 | 0.36   | 0.25     | 0.21   |
| Derby-10.3.1.4    | 0.12  | 0.36   | 0.35 | 0.42   | 0.46     | 0.40   |
| Groovy-1_6_2      | 0.22  | 0.11   | 0.12 | 0.55   | 0.18     | 0.13   |
| Hbase-0.94.0      | 0.24  | 0.17   | 0.16 | 0.32   | 0.37     | 0.32   |
| Hive-0.10.0       | 0.13  | 0.16   | 0.17 | 0.25   | 0.24     | 0.25   |
| Jruby-1.5.0       | 0.41  | 0.26   | 0.27 | 0.32   | 0.21     | 0.28   |
| Wicket-1.3.a-1    | 0.29  | 0.13   | 0.12 | 0.20   | 0.17     | 0.13   |
| Ant-1.3           | 0.33  | 0.25   | 0.24 | 0.26   | 0.33     | 0.26   |
| Ivy-2.0           | 0.28  | 0.20   | 0.21 | 0.23   | 0.25     | 0.28   |
| Jedit-4.1         | 0.48  | 0.31   | 0.30 | 0.35   | 0.42     | 0.39   |
| Log4j-1.0         | 0.48  | 0.28   | 0.29 | 0.24   | 0.45     | 0.36   |
| Synapse-1.2       | 0.53  | 0.27   | 0.26 | 0.33   | 0.49     | 0.43   |
| Tomcat            | 0.32  | 0.21   | 0.22 | 0.27   | 0.22     | 0.18   |
| Xalan-2.4         | 0.34  | 0.28   | 0.27 | 0.37   | 0.30     | 0.26   |
| Ar3               | 0.33  | 0.23   | 0.24 | 0.45   | 0.28     | 0.23   |
| Ar4               | 0.39  | 0.34   | 0.34 | 0.45   | 0.38     | 0.34   |
| Ar5               | 0.59  | 0.38   | 0.39 | 0.23   | 0.52     | 0.57   |
| Ar6               | 0.28  | 0.25   | 0.24 | 0.31   | 0.24     | 0.17   |
| **Average**       | **0.34**  | 0.26   | 0.26 | 0.31   | 0.32     | 0.29   |


## F1-Score Comparison of the Proposed MiTSA Method Against State-of-the-Art CPDP Baseline Methods

The table below presents the F1-score comparison of the proposed **MiTSA** model against CPDP Methods.

| Target Project     | MiTSA | FEDL | MASTER | SSE  | 3SW-MSTL | ARRAY |
|-------------------|-------|------|--------|------|----------|--------|
| Equinox           | 0.55  | 0.69 | 0.72   | 0.70 | 0.42     | 0.70   |
| Jdt               | 0.44  | 0.50 | 0.46   | 0.36 | 0.21     | 0.47   |
| Lucene            | 0.38  | 0.33 | 0.34   | 0.26 | 0.38     | 0.30   |
| Mylyn             | 0.44  | 0.41 | 0.32   | 0.35 | 0.19     | 0.30   |
| Pde               | 0.31  | 0.38 | 0.30   | 0.32 | 0.27     | 0.35   |
| Activemq-5.2.0    | 0.56  | 0.44 | 0.30   | 0.49 | 0.38     | 0.36   |
| Derby-10.3.1.4    | 0.58  | 0.59 | 0.55   | 0.59 | 0.31     | 0.59   |
| Groovy-1_6_2      | 0.39  | 0.26 | 0.25   | 0.34 | 0.18     | 0.27   |
| Hbase-0.94.0      | 0.48  | 0.55 | 0.42   | 0.38 | 0.39     | 0.48   |
| Hive-0.10.0       | 0.47  | 0.36 | 0.44   | 0.43 | 0.44     | 0.40   |
| Jruby-1.5.0       | 0.35  | 0.33 | 0.23   | 0.27 | 0.45     | 0.34   |
| Wicket-1.3.a-1    | 0.27  | 0.27 | 0.12   | 0.20 | 0.23     | 0.25   |
| Ant-1.3           | 0.38  | 0.49 | 0.40   | 0.34 | 0.41     | 0.45   |
| Ivy-2.0           | 0.40  | 0.33 | 0.38   | 0.24 | 0.42     | 0.36   |
| Jedit-4.1         | 0.53  | 0.54 | 0.56   | 0.44 | 0.40     | 0.56   |
| Log4j-1.0         | 0.58  | 0.52 | 0.54   | 0.42 | 0.54     | 0.60   |
| Synapse-1.2       | 0.54  | 0.56 | 0.56   | 0.51 | 0.52     | 0.55   |
| Tomcat            | 0.35  | 0.27 | 0.41   | 0.31 | 0.34     | 0.31   |
| Xalan-2.4         | 0.40  | 0.37 | 0.43   | 0.32 | 0.33     | 0.42   |
| Ar3               | 0.39  | 0.23 | 0.41   | 0.32 | 0.50     | 0.39   |
| Ar4               | 0.53  | 0.31 | 0.51   | 0.37 | 0.38     | 0.52   |
| Ar5               | 0.66  | 0.50 | 0.68   | 0.61 | 0.75     | 0.61   |
| Ar6               | 0.34  | 0.26 | 0.28   | 0.23 | 0.31     | 0.30   |
| **Average**       | **0.45** | 0.41 | 0.42   | 0.38 | 0.38     | 0.43   |
