# HE-PROJ-ACT-001 — Periodic-Activation Representational Bound

Identifier: `HE-PROJ-ACT-001`  
Status: active after this PR  
Parents: `HE-PROJ-001`, `HE-PROJ-003`  
Claim grade: theorem-grade for the Lipschitz/contraction theorem; worked-falsification-grade for the prime-wave example  
Anti-seed: `A-HE-PROJ-ACT-001`, `A-HE-PROJ-001`, `A-HE-PROJ-004`  
Scope: single-layer periodic activation as a Lipschitz lift; task tier and physical-constant interpretations out of scope

## Purpose

`HE-PROJ-001` constructs observer-level Markov kernels from projected deterministic substrate dynamics.

`HE-PROJ-003` proves that semantic distortion contracts according to the semantic Wasserstein / Dobrushin coefficient of the induced kernel.

`HE-PROJ-ACT-001` specializes that metric-measure contraction principle to neural activation maps. A single activation layer is a lift from an input trace to a representation trace. If the lift is Lipschitz, its stability is controlled by the same contraction calculus.

The result is useful for periodic activations, including SIREN-style sine activations and prime-wave-style periodic probes. The theorem is not a physical-constant result.

## Setup

Let:

```text
Phi(x) = phi(w x + b)
```

where:

- `x` is a scalar trace coordinate;
- `w,b in R` are fixed parameters;
- `phi : R -> R` is a periodic activation;
- `phi` is `L_phi`-Lipschitz on the domain under consideration.

Let `S` be a downstream semantic/readout map with Lipschitz constant `L_S`.

Let `K` be the induced Markov kernel on the observed trace process, and let `delta(K)` be the relevant contraction coefficient. In the total-variation case this is the Dobrushin coefficient. In the semantic-metric case it is `delta_sem(K)` from `HE-PROJ-003`.

## Lemma 1 — Activation layer Lipschitz constant

If `phi` is `L_phi`-Lipschitz, then:

```text
Lip(Phi) <= |w| L_phi
```

If `S` is `L_S`-Lipschitz, then:

```text
Lip(S o Phi) <= L_S |w| L_phi
```

### Proof

For `x,x'`:

```text
|Phi(x) - Phi(x')|
  = |phi(w x + b) - phi(w x' + b)|
  <= L_phi |w| |x - x'|
```

Composing with `S` multiplies the Lipschitz constants.

## Theorem 1 — Activation contraction bound

Under the setup above, semantic distortion through one activation/readout step is bounded by:

```text
rho <= L_S |w| L_phi delta(K)
```

where `delta(K)` is the contraction coefficient of the induced trace kernel in the chosen metric.

If:

```text
L_S |w| L_phi delta(K) < 1
```

then the activation/readout layer is contractive for semantic distortion. If the quantity is `>= 1`, this theorem gives no stability guarantee.

### Proof

By `HE-PROJ-003`, distortion under kernel action contracts by the kernel contraction coefficient. The activation/readout lift is `L_S |w| L_phi`-Lipschitz by Lemma 1. Composing the kernel contraction with the lift multiplies the bounds, giving:

```text
rho <= L_S |w| L_phi delta(K)
```

The contraction statement follows immediately when `rho < 1`.

## Band-limited single-periodic corollary

Assume additionally that `phi` is band-limited with dominant angular frequency `omega` and finite Fourier support. Then `Phi(x)=phi(wx+b)` can generate frequencies only in the rescaled support:

```text
freq(Phi) subset |w| freq(phi)
```

For the pure sine case:

```text
phi(t) = sin(omega t)
```

`Phi` has frequency `|w| omega` in `x`.

Therefore a single fixed pure-periodic unit cannot stably represent out-of-support frequency content. Any fit to frequency content outside its generated support is a sample-specific fit, not a stable representation. Broader periodic dictionaries or depth are required to represent broader spectra.

This corollary is a representational-capacity statement under a band-limited / finite-dictionary assumption. It is not a universal theorem about every bounded periodic function.

## Tangent-wave caveat

The prime-wave construction uses a tangent composition of the form:

```text
tanh(tan(theta))
```

This map is bounded, but the tangent poles make the raw composition discontinuous across the poles unless a branch convention, clipping, or regularization is specified. Boundedness is not Lipschitzness.

Therefore the raw tangent-wave construction is not a globally Lipschitz activation on the full circle. It can be treated under this theorem only on pole-free intervals, under a clipped/regularized version, or as an empirical periodic probe rather than as a globally Lipschitz activation.

This caveat is load-bearing. It prevents this theorem from being misread as a proof about unregularized `tanh(tan(theta))` on the full circle.

## Worked example — prime-wave falsification

The historical prime-wave construction has the form:

```text
wave(n) = tanh(tan(rad(P n + h)))
P = alpha (pi + 1/55)
h = 8
```

It was tested as a single periodic probe for prime positions.

The falsification record states:

- parameters fit on primes up to `1000` produced high in-sample circular cluster score;
- the same locked parameters evaluated on primes from `1000` to `120000` collapsed out of sample;
- random-integer controls produced the same in-sample/out-of-sample behavior;
- therefore the apparent fit was interpolation / parameter locking, not stable representation.

This is exactly the failure mode predicted by the activation contraction / finite-dictionary view: a single periodic probe can fit a finite sample without representing the underlying arithmetic structure out of sample.

The worked example is recorded as falsification evidence, not as a physical or number-theoretic theorem.

## Relationship to Heller-Winters prime-circle work

`HW-PRIME-CIRCLE-001` in Heller-Winters identifies the prime-circle construction as primorial-wheel arithmetic and records the Jacobsthal maximal-gap correspondence. That result is number-theoretic and survives independently of the prime-wave falsification.

`HE-PROJ-ACT-001` addresses a different question: whether a single periodic activation/probe can stably represent the prime sequence. The answer recorded here is negative for the historical prime-wave probe under locked-parameter testing.

The two results are compatible:

- Heller-Winters: the prime-circle seed work has a real arithmetic object — primorial wheels and Jacobsthal gaps.
- Heller-Einstein: the single periodic activation/probe is not a stable representation of primes out of sample.

## What this document establishes

This document establishes:

1. A Lipschitz activation/readout layer has distortion bound:

```text
rho <= L_S |w| L_phi delta(K)
```

2. A pure single-periodic activation generates only its rescaled frequency support.
3. The historical prime-wave probe is falsified as a stable out-of-sample prime representation.
4. The tangent-wave construction needs a pole/regularization caveat before it can be treated as a global Lipschitz activation.

## What this document does not establish

This document does not:

- derive the fine-structure constant or any other physical constant;
- claim that primes are represented by a single periodic activation;
- prove a theorem about the Riemann hypothesis, zeta zeros, or prime gaps;
- prove a multi-layer periodic-network approximation theorem;
- prove task-tier stability (`HE-PROJ-TASK-001` remains reserved);
- derive quantum mechanics, Born rule, noncommuting observables, or entanglement;
- assert physical substrate uniqueness;
- transfer methodology into any Clay-program proof.

## Reserved follow-ups

- `HE-PROJ-ACT-002` — multi-layer periodic dictionary / depth multiplication theorem, reserved.
- `HE-PROJ-ACT-003` — regularized tangent-wave activation analysis, reserved.
- `HE-PROJ-ACT-004` — formal prime-wave falsification replay with receipts, reserved.

## Citation form

```text
[HE-PROJ-ACT-001 @ <merge-sha>]
[A-HE-PROJ-ACT-001 @ <merge-sha>]
[HE-PROJ-001 @ e57f8f386c412ff68283783d3e7142bef81503d9]
[HE-PROJ-003 @ 0dc1c59613ce1f598f28ac1cd62357e9d2ff06e9]
```

## Versioning

This is `HE-PROJ-ACT-001 v1.0`. Stronger frequency-ceiling or multi-layer claims require separate statements with explicit assumptions and proofs.
