# Typed Interface Ontology

Status: canonical Heller-Einstein v0.1 interface ontology surface.  
Source: Einstein-Heller Interface Program v1.7 verified source candidate.  
Claim level: verified formal core as marked below.  
Primary identifiers: `HE-INT-*`, `HE-PLC-*`, `HE-SH-*`.

## Purpose

This document imports the verified formal core of the v1.7 Einstein-Heller source candidate into repository-native form.

It defines typed access chains, observer-relative trace maps, semantic lifts, reconstruction maps, latent fibers, placeholder spaces, semantic equivalence, sufficiency hierarchy, and the semantic right-inverse criterion.

## HE-INT-001 — Typed access chain

Grade: verified formal core / foundational interface vocabulary.

Let `X` denote the latent or bulk state space. Let bulk dynamics be represented by:

```text
Phi_t : X -> X
x_t = Phi_t(x_0)
```

For observer `O`, define a trace space:

```text
Y_O
```

and trace map:

```text
tau_O : X -> Y_O
```

Define an observer-relative semantic lift:

```text
S_O : Y_O -> M_O
```

The typed access chain is:

```text
x_t in X --tau_O--> y_t in Y_O --S_O--> m_t in M_O
```

Meaning is not inserted as a primitive bulk field. Meaning is an observer-relative lift from interface traces.

## HE-INT-002 — Reconstruction map and latent fiber

Grade: verified formal core / foundational interface vocabulary.

A reconstruction map, when available, is:

```text
R_O : Y_O -> X
```

For a trace `y in Y_O`, the compatible latent fiber is:

```text
F_y := tau_O^{-1}(y)
```

A many-to-one trace map creates nontrivial latent fibers. Those fibers are the formal site where deterministic latent dynamics can induce stochastic observer-level dynamics when projected.

## HE-INT-003 — Observer-relative semantic equivalence

Grade: verified formal core / foundational interface vocabulary.

Observer-relative semantic equivalence is:

```text
x ~_O x' iff S_O(tau_O(x)) = S_O(tau_O(x'))
```

This is an equivalence at the observer-interface semantic level. It is not an identity statement about latent bulk states.

## HE-PLC-001 — Placeholder chain

Grade: method-grade placeholder discipline.

The semantic-geometry placeholder chain is:

```text
X_15 -> X_7 -> X_3 -> X_2
```

These are typed placeholders, not topological commitments.

No claim is made here that the placeholders are literal spheres, homogeneous spaces, or bundle bases.

## HE-SH-001 — Pointwise reconstruction error

Grade: verified formal core / sufficiency vocabulary.

Pointwise reconstruction error is:

```text
epsilon_rec^O(x) := d_X(x, R_O(tau_O(x)))
```

This measures microstate reconstruction error after passing through the observer trace and reconstruction map.

## HE-SH-002 — Strong microstate sufficiency

Grade: verified formal core / sufficiency vocabulary.

Strong microstate sufficiency on `U subset X` is:

```text
R_O o tau_O = id_U
```

This is a strong condition. It implies semantic sufficiency but is not required for semantic or task sufficiency.

## HE-SH-003 — Semantic distortion

Grade: verified formal core / sufficiency vocabulary.

Semantic distortion is:

```text
delta_sem^O(x) := d_M(S_O(tau_O(x)), S_O(tau_O(R_O(tau_O(x)))))
```

Semantic distortion can be small even when microstate reconstruction is incomplete.

## HE-SH-004 — Task distortion

Grade: method-grade sufficiency vocabulary.

Task distortion is defined analogously after applying an observer-relative action map:

```text
A_O : M_O -> A_O_space
```

and a task loss:

```text
ell_A
```

Task sufficiency is task-relative. It is not equivalent to semantic sufficiency or microstate sufficiency.

## HE-SH-005 — Semantic holography regime

Grade: method-grade regime vocabulary.

Semantic holography is the regime where semantic or task distortion is small while microstate reconstruction remains incomplete.

It does not claim that ontology collapses to the boundary.

## HE-SH-006 — Semantic right-inverse criterion

Grade: verified formal core / criterion.

If:

```text
S_O o tau_O o R_O o tau_O = S_O o tau_O on U
```

then the interface is strongly semantically sufficient on `U`.

Microstate sufficiency implies semantic sufficiency. Semantic sufficiency does not imply microstate sufficiency.

## Non-claims

This document does not claim observer-independent semantic lift.

This document does not claim ontology collapses to the boundary.

This document does not claim placeholder spaces are literal spheres, homogeneous spaces, or bundle bases.

This document does not derive quantum mechanics, the Born rule, noncommuting observables, or entanglement structure.

This document does not transfer proof content into Heller-Godel, Heller-Dirac, or any Clay-program repository.
