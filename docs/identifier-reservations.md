# Heller-Einstein Identifier Reservations

Status: namespace reservation and governance record.

## Active identifiers

| Identifier | Role | Path |
|---|---|---|
| `HE-INT-001` | Formal interface ontology spec: typed access chain, trace maps, semantic lifts, reconstruction maps, latent fibers, semantic equivalence | `docs/interface/HE-INT-001-interface-ontology.md` |
| `HE-PROJ-001` | Projection-induced Markov kernel theorem | `docs/projection/HE-PROJ-001-projection-induced-stochasticity.md` |
| `HE-PROJ-002` | Sufficiency hierarchy and semantic holography; microstate implies semantic sufficiency; converse counterexample; rate-distortion framing | `docs/projection/HE-PROJ-002-sufficiency-hierarchy.md` |
| `HE-PROJ-003` | Metric-measure bridge for semantic stability; semantic pseudometric and Wasserstein contraction theorem | `docs/projection/HE-PROJ-003-metric-measure-bridge.md` |
| `HE-PROJ-INV-001` | Markov kernel realizability theorem | `docs/projection/HE-PROJ-INV-001-markov-kernel-realizability.md` |
| `HE-PROJ-INV-003` | Markov shift identifiability theorem for finite stationary observer-generated invertible realizations | `docs/projection/HE-PROJ-INV-003-markov-shift-identifiability.md` |
| `HE-PHYS-001` | Conservative physical-core action; seven-sector microscopic action, minimal Einstein-Cartan torsion-elimination contact term, observer-interface term | `docs/physics/HE-PHYS-001-conservative-physical-core-action.md` |
| `HE-EX-001` | Discrete phase cycle on `Z_12` with two-cell trace and kernel `[[2/3,1/3],[1/3,2/3]]` | `docs/examples/HE-EX-001-discrete-phase-cycle.md` |
| `HE-EX-002` | Continuous phase flow on `S^1` with matched kernel | `docs/examples/HE-EX-002-continuous-phase-flow.md` |

## Withdrawn namespace

### HE-FND-* — withdrawn / consolidated under HE-INT-*

Bootstrap reserved `HE-FND-*` as a possible foundational-vocabulary namespace. This split is withdrawn. Heller-Einstein's foundational vocabulary is the interface ontology, canonicalized under `HE-INT-001`.

Future content should cite `HE-INT-001` rather than `HE-FND-*` for typed access-chain vocabulary, trace maps, semantic lifts, reconstruction maps, latent fibers, and observer-relative semantic equivalence.

## Reserved identifiers

### HE-INT-* — Interface ontology

| Identifier | Role | Status |
|---|---|---|
| `HE-INT-001` | Formal interface ontology spec | active |
| `HE-INT-002` | Reconstruction refinements and admissible partial inverses beyond HE-INT-001 base definitions | reserved |
| `HE-INT-003` | Observer comparison / inter-observer translation maps | reserved |
| `HE-INT-004..010` | Reserved | future |

### HE-PROJ-* — Projection-induced stochasticity

| Identifier | Role | Status |
|---|---|---|
| `HE-PROJ-001` | Projection-induced Markov kernel theorem | active |
| `HE-PROJ-002` | Sufficiency hierarchy and semantic holography | active |
| `HE-PROJ-003` | Metric-measure bridge for semantic stability | active |
| `HE-PROJ-004..010` | Reserved | future |
| `HE-PROJ-INV-001` | Markov kernel realizability theorem | active |
| `HE-PROJ-INV-002` | Minimal realization problem | reserved; open |
| `HE-PROJ-INV-003` | Markov shift identifiability theorem | active |
| `HE-PROJ-INV-004` | Countable-state stationary Markov-shift extension | reserved |
| `HE-PROJ-INV-005` | Non-stationary / sigma-finite natural-extension problem | reserved |
| `HE-PROJ-TASK-001` | Task-sufficiency lattice and task-family infimum structure | reserved |

### HE-PHYS-* — Conservative physical core

| Identifier | Role | Status |
|---|---|---|
| `HE-PHYS-001` | Conservative physical-core action; transcription-grade / rendered-page verified | active |
| `HE-PHYS-002` | Equations of motion and convention-checked variational derivatives | reserved |
| `HE-PHYS-003` | Effective torsion-eliminated action details and convention crosswalk | reserved |
| `HE-PHYS-004` | Interface boundary conditions on observer hypersurface | reserved |
| `HE-PHYS-005..010` | Reserved | future |

### HE-PLC-* — Placeholder spaces

| Identifier | Role | Status |
|---|---|---|
| `HE-PLC-001` | Typed placeholder chain `X_15 -> X_7 -> X_3 -> X_2` | reserved |
| `HE-PLC-002..005` | Reserved | future |

### HE-EX-* — Canonical exemplars

| Identifier | Role | Status |
|---|---|---|
| `HE-EX-001` | Discrete phase cycle on `Z_12` with two-cell trace and kernel `[[2/3,1/3],[1/3,2/3]]` | active |
| `HE-EX-002` | Continuous phase flow on `S^1` with matched kernel | active |
| `HE-EX-003..005` | Standards-grounded interface examples | future |

### HE-MTH-* — Methodology

| Identifier | Role | Status |
|---|---|---|
| `HE-MTH-001` | Structural-cognate map to Heller-Dirac `HD-*` identifiers | reserved |
| `HE-MTH-002..005` | Reserved | future |

### A-HE-* — Anti-seed register

The following anti-seed identifiers are active in `docs/anti-seed-einstein.md`:

| Identifier | Failure mode |
|---|---|
| `A-HE-FND-001` | Speculative content scope discipline |
| `A-HE-INT-001` | Ontology does not collapse to boundary |
| `A-HE-INT-002` | Semantic lift is observer-relative |
| `A-HE-PROJ-001` | Projection-induced stochasticity does not derive quantum mechanics |
| `A-HE-PROJ-002` | Sufficiency hierarchy tiers are distinct |
| `A-HE-PROJ-003` | Universal realizability is not explanation |
| `A-HE-PROJ-004` | Semantic stability is not task stability or microstate recovery |
| `A-HE-PROJ-005` | Canonical Markov shift is not physical substrate uniqueness |
| `A-HE-PHYS-001` | Conservative core is not Standard Model derivation |
| `A-HE-PHYS-002` | Algebraic torsion is the minimal branch |
| `A-HE-PHYS-003` | Boundary term completion depends on boundary data |
| `A-HE-PHYS-004` | Action transcription is not convention verification |
| `A-HE-PLC-001` | Placeholder spaces are typed, not topological |
| `A-HE-EX-001` | Exemplars are fixture-grade |
| `A-HE-MTH-001` | Universal Bridge constraint applies analogously |

## Activation rule

A reserved `HE-*` identifier becomes active only when a PR adds a dedicated specification or fixture file and updates this registry. Downstream consumers must cite active identifiers only, unless explicitly citing a reservation as pending work.
