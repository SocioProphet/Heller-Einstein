# HE-PROJ-ACT-002 — Multi-Layer Activation Contraction Bound

Identifier: `HE-PROJ-ACT-002`  
Status: active after this PR  
Parents: `HE-PROJ-ACT-001`, `HE-PROJ-003`  
Claim grade: theorem-grade for Lipschitz/contraction composition; reservation-grade for spectral attainability/frontier statements  
Anti-seed: `A-HE-PROJ-ACT-001`, `A-HE-PROJ-ACT-002`  
Scope: depth-`d` composition of Lipschitz activation layers; task tier and spectral-attainability claims out of scope

## Purpose

`HE-PROJ-ACT-001` proved the single-layer activation contraction bound:

```text
rho <= L_S |w| L_phi delta(K)
```

for a Lipschitz activation/readout lift over an induced trace kernel.

This document extends the rigorous part of that result to depth `d`: the Lipschitz constants multiply, and the semantic-distortion contraction bound multiplies accordingly.

It also records the key correction: a product of Lipschitz constants is **not** a theorem about Fourier support. Multi-layer periodic networks can generate harmonics through nonlinear composition. Therefore a frequency-product ceiling or attainability statement is not active here. It is reserved as `HE-PROJ-ACT-INV-001`.

## Setup

Let a depth-`d` scalar activation chain be:

```text
N_d = Phi_d o Phi_{d-1} o ... o Phi_1
```

with:

```text
Phi_i(u) = phi_i(w_i u + b_i)
```

where each `phi_i` is `L_phi_i`-Lipschitz on the domain under consideration.

Let:

```text
A_i := |w_i| L_phi_i
```

and let downstream readout `S` be `L_S`-Lipschitz.

Let `K` be the induced trace kernel and let `delta(K)` denote the relevant contraction coefficient, e.g. the Dobrushin coefficient or `delta_sem(K)` from `HE-PROJ-003`.

## Theorem 1 — Lipschitz product for depth-d activation chains

The depth-`d` chain `N_d` is Lipschitz with:

```text
Lip(N_d) <= product_{i=1}^d A_i
          = product_{i=1}^d |w_i| L_phi_i
```

and the readout-composed map satisfies:

```text
Lip(S o N_d) <= L_S product_{i=1}^d |w_i| L_phi_i
```

### Proof

Each layer satisfies:

```text
Lip(Phi_i) <= |w_i| L_phi_i = A_i
```

by `HE-PROJ-ACT-001`. Lipschitz constants compose multiplicatively:

```text
Lip(Phi_d o ... o Phi_1) <= Lip(Phi_d) ... Lip(Phi_1)
```

so:

```text
Lip(N_d) <= product_i A_i
```

Composing with `S` multiplies by `L_S`.

## Theorem 2 — Multi-layer activation contraction bound

Under the setup above, semantic distortion through the depth-`d` activation/readout chain is bounded by:

```text
rho_d <= L_S (product_{i=1}^d |w_i| L_phi_i) delta(K)
```

If:

```text
L_S (product_{i=1}^d |w_i| L_phi_i) delta(K) < 1
```

then the depth-`d` activation/readout chain is contractive for semantic distortion. If the quantity is `>= 1`, this theorem provides no stability guarantee.

### Proof

`HE-PROJ-003` gives contraction by `delta(K)` under the kernel action. The depth-`d` activation/readout lift has Lipschitz constant bounded by Theorem 1. Multiplying the two bounds gives the stated inequality.

## Corollary — Uniform-layer stability criterion

If all layers have a common bound:

```text
A_i <= A
```

then:

```text
rho_d <= L_S A^d delta(K)
```

Therefore:

- if `A < 1`, increasing depth improves the contraction bound geometrically;
- if `A = 1`, depth neither improves nor worsens the Lipschitz part of the bound;
- if `A > 1`, increasing depth worsens the worst-case stability bound.

This is a stability statement only. It is not an expressivity theorem.

## Spectral caveat — Lipschitz bounds are not Fourier-support bounds

The tempting but invalid claim is:

```text
f_max^{(d)} = product_i f_max^{(i)}
```

or even that the product is always a rigorous Fourier-support ceiling.

This document does **not** assert that claim.

Reason: a nonlinear periodic activation can generate harmonics. Even if a layer begins with a simple sine activation, composition such as:

```text
sin(a sin x)
```

has a Fourier-Bessel expansion containing infinitely many harmonics. Thus frequency content is not a scalar that simply multiplies through the network. It spreads.

The Lipschitz product controls stability and variation. It does not, by itself, bound Fourier support.

## Safe representational statement

The safe statement is:

> A depth-`d` activation network cannot claim stable representation of a signal unless it satisfies both a stability condition and a spectral/support condition appropriate to the chosen activation class.

The stability condition is the theorem above:

```text
L_S (product_i |w_i| L_phi_i) delta(K) < 1
```

The spectral/support condition is not solved in this PR. It depends on the activation dictionary, harmonic-generation structure, weight choices, and the chosen notion of representation.

For finite Fourier dictionaries, one can define an effective generated support `B_d` recursively from the dictionary and weights. For general smooth periodic activations, `B_d` may be infinite even when the Lipschitz product is finite.

## Reserved frontier — HE-PROJ-ACT-INV-001

The open attainability/frontier problem is reserved as `HE-PROJ-ACT-INV-001`:

```text
Given a periodic activation dictionary D, depth d, weights (w_i), and a representation norm,
characterize the effective spectral support / bandwidth B_d that is stably attainable
under the multi-layer contraction constraint.
```

Open subquestions:

1. When does depth multiply usable bandwidth rather than merely generate small-amplitude harmonics?
2. What harmonic-alignment conditions are necessary for a product-style ceiling to be tight?
3. How do Lipschitz stability and spectral richness trade off?
4. Which activation dictionaries admit computable `B_d`?
5. What lower-bound theorem can be stated for prime-sequence representation once `B_d` is known?

This PR does not solve those questions.

## Prime-sequence consequence

`HE-PROJ-ACT-001` records the historical prime-wave probe as a locked-parameter falsification. That negative result remains active.

This document adds only a structural conclusion:

- a deeper network changes the stability bound via the product of layer Lipschitz constants;
- a deeper network may generate richer harmonics;
- no specific depth is guaranteed to represent primes until `HE-PROJ-ACT-INV-001` or a later dictionary-specific theorem characterizes the attainable spectral support.

Therefore the correct statement is:

> The prime-wave falsification rules out the historical single periodic probe. It does not by itself prove a quantitative minimum depth for all periodic networks.

A quantitative minimum-depth theorem for primes is reserved. It requires a concrete activation dictionary, spectral-support definition, and out-of-sample validation protocol.

## What this document establishes

This document establishes:

1. Depth-`d` Lipschitz constants multiply:

```text
Lip(N_d) <= product_i |w_i| L_phi_i
```

2. Depth-`d` semantic-distortion contraction is bounded by:

```text
rho_d <= L_S (product_i |w_i| L_phi_i) delta(K)
```

3. Uniform-layer stability follows from `rho_d <= L_S A^d delta(K)`.
4. Frequency-product claims are not licensed by Lipschitz theory alone.
5. Spectral attainability is a separate open problem, reserved as `HE-PROJ-ACT-INV-001`.

## What this document does not establish

This document does not:

- prove that representational bandwidth equals a product of layer frequencies;
- prove a minimum depth for prime-sequence representation;
- prove that any multi-layer periodic network represents primes;
- prove a multi-layer SIREN approximation theorem;
- analyze unregularized `tanh(tan(theta))` across tangent poles;
- derive a physical constant;
- prove RH, zeta, or prime-gap claims;
- prove task-tier stability;
- change upstream pins.

## Anti-seed cross-reference

`A-HE-PROJ-ACT-002` records the boundary: multi-layer Lipschitz contraction is a stability bound, not a frequency-attainability or representability guarantee.

## Citation form

```text
[HE-PROJ-ACT-002 @ <merge-sha>]
[A-HE-PROJ-ACT-002 @ <merge-sha>]
[HE-PROJ-ACT-001 @ a5f9b9113d3b883920368241e0bf9f46264d3bae]
[HE-PROJ-003 @ 0dc1c59613ce1f598f28ac1cd62357e9d2ff06e9]
```

## Versioning

This is `HE-PROJ-ACT-002 v1.0`. It is intentionally narrower than the originally proposed frequency-product theorem. Stronger spectral or minimum-depth claims require `HE-PROJ-ACT-INV-001` or a successor theorem.
