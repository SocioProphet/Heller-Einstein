# HE-INT-001 — Formal Interface Ontology

Identifier: `HE-INT-001`  
Distance tier: framework-foundational interface ontology  
Status: active after this PR  
Anti-seed: `A-HE-INT-001`, `A-HE-INT-002`, `A-HE-PROJ-001`, `A-HE-MTH-001`

## Consolidation decision

`HE-INT-001` is the single parent specification for Heller-Einstein interface ontology.

Bootstrap reservations had separated `HE-FND-*` from `HE-INT-*`. That split is withdrawn in this PR. Heller-Einstein's foundational vocabulary is interface ontology, and maintaining a separate near-empty `HE-FND-*` namespace would force future content to cite two identifiers where one suffices.

Accordingly:

- `HE-INT-001` is active and load-bearing for typed access-chain vocabulary.
- `HE-FND-*` is withdrawn as a separate namespace.
- HE-FND-* is withdrawn; cite `HE-INT-001` for foundational interface vocabulary.
- Future foundational Heller-Einstein content should extend `HE-INT-*`, `HE-PROJ-*`, `HE-PHYS-*`, `HE-PLC-*`, or `HE-MTH-*` as appropriate.

## Typed access chain

Let `X` be the latent or bulk state space. Bulk dynamics may be written:

```text
Phi_t : X -> X
x_t = Phi_t(x_0)
```

For observer `O`, define a trace space `Y_O` and a trace map:

```text
tau_O : X -> Y_O
```

Define an observer-relative semantic space `M_O` and semantic lift:

```text
S_O : Y_O -> M_O
```

The typed access chain is:

```text
x_t in X --tau_O--> y_t in Y_O --S_O--> m_t in M_O
```

where:

```text
y_t = tau_O(x_t)
m_t = S_O(y_t)
```

Meaning is not a primitive bulk field. Meaning is an observer-relative lift from interface traces.

## Trace fibers

For `y in Y_O`, define the compatible latent fiber:

```text
F_y := tau_O^{-1}(y) = {x in X : tau_O(x) = y}
```

The fiber is the set of latent states compatible with the same observer trace.

When `tau_O` is many-to-one, the observer loses microstate information. `HE-PROJ-001` turns this lost information into an induced Markov kernel once a fiber measure is supplied.

## Semantic equivalence

Observer-relative semantic equivalence is:

```text
x ~_O x' iff S_O(tau_O(x)) = S_O(tau_O(x'))
```

This relation is observer-relative. Different observers may have different trace maps, semantic spaces, and semantic lifts.

Per `A-HE-INT-002`, the semantic lift is observer-relative by definition.

## Reconstruction maps

When available, a reconstruction map is:

```text
R_O : Y_O -> X
```

A reconstruction map selects a representative latent state compatible with a trace. In general:

```text
tau_O(R_O(y)) = y
```

may hold only on a declared domain of admissible traces, and it does not imply full microstate recovery unless explicitly stated.

## Interface laws

### Trace compatibility

An observer trace is compatible with a latent state when:

```text
tau_O(x) = y
```

Compatibility is fiber membership:

```text
x in F_y
```

### Semantic preservation

A reconstruction map is semantically preserving on a subset `U subseteq X` when:

```text
S_O(tau_O(R_O(tau_O(x)))) = S_O(tau_O(x))
```

for all `x in U`.

This is weaker than microstate reconstruction.

### Microstate reconstruction

A reconstruction map is microstate-exact on `U subseteq X` when:

```text
R_O(tau_O(x)) = x
```

for all `x in U`.

Microstate reconstruction implies semantic preservation, but semantic preservation does not imply microstate reconstruction.

## Relationship to HE-PROJ-001

`HE-PROJ-001` depends on the following `HE-INT-001` objects:

- trace map `tau : X -> Y`;
- fiber `F_y = tau^{-1}(y)`;
- observer-level trace space `Y`;
- the distinction between latent determinism and observer-level law.

`HE-PROJ-001` adds probability measures `mu_y` on fibers and constructs a Markov kernel:

```text
K(y, B) = mu_y({x in F_y : tau(f(x)) in B})
```

`HE-INT-001` supplies the typed interface substrate. `HE-PROJ-001` supplies the stochasticity theorem.

## Boundary

This document does not:

- collapse ontology to boundary traces;
- make meaning observer-independent;
- claim that reconstruction is generally possible;
- derive quantum mechanics;
- derive the Born rule;
- assert that all probability is projection-induced;
- specify Einstein-Cartan-Dirac physical dynamics.

It formalizes the interface vocabulary used by later `HE-*` content.

## Citation form

```text
[HE-INT-001 @ <merge-sha>]
[A-HE-INT-001 @ <merge-sha>]
[A-HE-INT-002 @ <merge-sha>]
```

## Versioning

This is `HE-INT-001 v1.0`. Future changes that alter the typed access-chain structure require a major-version update and downstream migration review.
