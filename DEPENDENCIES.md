# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`); PFK substrate (`PFK-*`); framework anti-seed (`A-HG-*`, `A-PFK-*`) |

Heller-Dirac is not yet a dependency. When `HE-*` content explicitly cites `HD-*` content, a follow-up PR will add `SocioProphet/Heller-Dirac` as a second upstream pin.

## Cited objects

### Framework-grade

| Identifier | Role |
|---|---|
| `HG-FND-*` | Foundational vocabulary |
| `HG-MTH-005` | Universal Bridge formal specification, cited as a method-grade constraint applying analogously to `HE-*` content |

### PFK operational substrate

| Identifier | Role |
|---|---|
| `PFK-SCHEMA-001..004` | Standard schemas for future receipt emission |
| `PFK-OP-001` | Event ingestion for future receipts |
| `PFK-OP-030` | Calibration operator for future exemplar baselines |

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
| `A-PFK-SCHEMA-002` | schema-version drift; pin is not floating |
| `A-PFK-VAL-001` | validator green is not audit completion |

## Forbidden edges

- `Heller-Einstein` -> any Clay-program repo.
- `Heller-Einstein` -> Heller-Godel-other-than-pinned-commit.
- `Heller-Einstein` -> Heller-Dirac before an explicit dependency PR adds it.

## Publisher contract

Heller-Einstein publishes `HE-*` identifiers for downstream consumption when content needs typed-interface or projection-induced-stochasticity apparatus.

Consumers cite Heller-Einstein at a pinned commit parallel to their Heller-Godel pin:

```text
[HE-INT-001 @ <heller-einstein-pin>]
[HG-FND-001 @ 988307215ad38ccb16514311222184a1b757752b]
```

Pinned commits are not floating.

## Citation form

```text
[HE-INT-001 @ <merge-sha>]
[HE-PROJ-001 @ <merge-sha>]
[HE-PHYS-001 @ <merge-sha>]
[HE-PLC-001 @ <merge-sha>]
[HE-EX-001 @ <merge-sha>]
[A-HE-INT-001 @ <merge-sha>]
```
