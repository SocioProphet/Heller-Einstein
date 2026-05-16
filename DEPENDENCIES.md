# Dependencies

## Upstream

This repository consumes from two upstream framework repositories after HE-PROJ-001.

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`); PFK substrate (`PFK-*`); framework anti-seed (`A-HG-*`, `A-PFK-*`) |
| `SocioProphet/Heller-Dirac` | `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993` | Heller-Dirac foundational reference surface (`HD-FND-*`); modular-flow cognate for HE-PROJ-*; Heller-Dirac anti-seed (`A-HD-*`) |

Both pins are fixed. Re-pinning requires an explicit dependency PR.

## Cited objects

### From Heller-Godel @ `988307215ad38ccb16514311222184a1b757752b`

| Identifier | Role |
|---|---|
| `HG-FND-*` | Foundational vocabulary |
| `HG-MTH-005` | Universal Bridge formal specification, cited as a method-grade constraint applying analogously to `HE-*` content |
| `PFK-SCHEMA-001..004` | Standard schemas for future receipt emission |
| `PFK-OP-001` | Event ingestion for future receipts |
| `PFK-OP-030` | Calibration operator for future exemplar baselines |

### From Heller-Dirac @ `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`

| Identifier | Role |
|---|---|
| `HD-FND-007` | Tomita-Takesaki modular operator and modular flow; structural cognate for trace-map induced observer-level evolution |
| `HD-FND-008` | KMS condition; structural cognate for observer-relative equilibrium / induced stochasticity comparisons |
| `A-HD-TM-001` | modular flow is not automatically physical time |
| `A-HD-FND-001` | HD-FND identifiers are reference surface, not reproof |

## Anti-seed surfaces

### Framework anti-seed

| Identifier | Applies because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs |
| `A-DOC-002` | Drive sources become provenance-only after repo canonicalization |

### PFK anti-seed

| Identifier | Applies because |
|---|---|
| `A-PFK-OP-001` | operator invocation is not evidence |
| `A-PFK-SCHEMA-001` | schema validity is not content validity |
| `A-PFK-SCHEMA-002` | schema-version drift; pins are not floating |
| `A-PFK-VAL-001` | validator green is not audit completion |

### Heller-Dirac anti-seed

| Identifier | Applies because |
|---|---|
| `A-HD-TM-001` | modular flow is not automatically physical time; modular-flow / trace-map-evolution comparison is method-grade only |
| `A-HD-FND-001` | HD-FND identifiers are reference surface, not new Heller-Einstein claims |

## Forbidden edges

- `Heller-Einstein` -> any Clay-program repo.
- `Heller-Einstein` -> Heller-Godel-other-than-pinned-commit.
- `Heller-Einstein` -> Heller-Dirac-other-than-pinned-commit.
- `Heller-Einstein` -> Heller-Dirac proof transfer. HE-PROJ-* and HD-TM-* are structurally cognate but mathematically distinct.

## Publisher contract

Heller-Einstein publishes `HE-*` identifiers for downstream consumption when content needs typed-interface or projection-induced-stochasticity apparatus.

Consumers cite Heller-Einstein at a pinned commit parallel to their Heller-Godel and Heller-Dirac pins when applicable.

## Citation form

```text
[HE-PROJ-001 @ <merge-sha>]
[HE-EX-001 @ <merge-sha>]
[HE-EX-002 @ <merge-sha>]
[HD-FND-007 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HE-PROJ-001 @ <merge-sha>]
[A-HD-TM-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```
