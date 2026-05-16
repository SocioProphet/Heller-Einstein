# HE-PROJ-003 — Metric–Measure Bridge for Semantic Stability

Identifier: `HE-PROJ-003`  
Parent interface ontology: `HE-INT-001`  
Parent projection theorem: `HE-PROJ-001`  
Parent sufficiency hierarchy: `HE-PROJ-002`  
Status: active after this PR  
Claim grade: theorem-grade for semantic tier  
Anti-seed: `A-HE-PROJ-001`, `A-HE-PROJ-002`, `A-HE-PROJ-004`

## Purpose

`HE-PROJ-001` is measure-theoretic: deterministic latent dynamics and fiber measures induce a Markov kernel on traces.

`HE-PROJ-002` is metric-theoretic: semantic distortion is measured in a semantic metric space.

`HE-PROJ-003` bridges them. It proves that the Markov kernel's contraction coefficient in the semantic pseudometric controls semantic stability under iteration.

Task-tier distortion is out of scope and remains reserved for `HE-PROJ-TASK-001`.

## Setup

Let `Y` be the observer trace space from `HE-INT-001`. Let:

```text
S : Y -> M
```

be an observer-relative semantic lift into a metric space `(M, d_M)`.

Define the pullback semantic pseudometric on `Y`:

```text
d_sem(y, y') := d_M(S(y), S(y'))
```

This is a pseudometric. It is a metric iff `S` is injective modulo the metric's null relation.

## Proposition 1 — Null set equals semantic equivalence

The zero set of `d_sem` is exactly the semantic equivalence relation from `HE-INT-001`:

```text
d_sem(y, y') = 0 iff S(y) = S(y')
```

When `y = tau(x)` and `y' = tau(x')`, this is:

```text
d_sem(tau(x), tau(x')) = 0 iff x ~_O x'
```

where:

```text
x ~_O x' iff S(tau(x)) = S(tau(x'))
```

Thus the pseudometric degeneracy is not an error; it is the metric expression of observer-relative semantic equivalence.

## Markov action

Let `K` be the Markov kernel on `Y` from `HE-PROJ-001`. For a probability measure `mu` on `Y`, define:

```text
(mu K)(B) := integral_Y K(y, B) dmu(y)
```

For a bounded measurable test function `phi : Y -> R`, define:

```text
K phi(y) := integral_Y phi(y') K(y, dy')
```

## Semantic Wasserstein contraction coefficient

Let `W_1^{d_sem}` denote the 1-Wasserstein distance on probability measures over `Y` using the cost `d_sem`.

Define:

```text
delta_sem(K) := sup_{d_sem(y,z) > 0} W_1^{d_sem}(K(y, .), K(z, .)) / d_sem(y,z)
```

where rows with `d_sem(y,z) = 0` are excluded. If no such pair exists, set `delta_sem(K) = 0`.

## Theorem 1 — Kantorovich–Dobrushin contraction

For probability measures `mu, nu` on `Y` with finite first moment:

```text
W_1^{d_sem}(mu K, nu K) <= delta_sem(K) W_1^{d_sem}(mu, nu)
```

## Proof

By Kantorovich–Rubinstein duality:

```text
W_1^{d_sem}(mu K, nu K) = sup_{Lip(phi) <= 1} | integral phi d(mu K) - integral phi d(nu K) |
```

Using the Markov action:

```text
integral phi d(mu K) = integral K phi dmu
```

For any `phi` with `Lip_{d_sem}(phi) <= 1`, we have:

```text
|K phi(y) - K phi(z)| <= W_1^{d_sem}(K(y,.), K(z,.)) <= delta_sem(K) d_sem(y,z)
```

so `K phi` is `delta_sem(K)`-Lipschitz. Therefore:

```text
| integral K phi dmu - integral K phi dnu | <= delta_sem(K) W_1^{d_sem}(mu, nu)
```

Taking the supremum over all 1-Lipschitz `phi` proves the theorem.

## Relation to total variation

Define the Dobrushin total-variation coefficient:

```text
delta_TV(K) := sup_{y,z} TV(K(y,.), K(z,.))
```

where:

```text
TV(alpha, beta) = (1/2) ||alpha - beta||_1
```

If `d_sem` has finite diameter:

```text
D_sem := sup_{y,z} d_sem(y,z) < infinity
```

then:

```text
W_1^{d_sem}(alpha, beta) <= D_sem TV(alpha, beta)
```

If additionally:

```text
d_min := inf_{d_sem(y,z)>0} d_sem(y,z) > 0
```

then:

```text
delta_sem(K) <= (D_sem / d_min) delta_TV(K)
```

For the discrete semantic metric `d_sem(y,z)=1` when `S(y) != S(z)` and `0` otherwise:

```text
D_sem = d_min = 1
```

and the sharp identity is:

```text
delta_sem(K) = delta_TV(K)
```

## Theorem 2 — Semantic distortion evolution

Let `mu_n` and `nu_n` be two trace-level distributions interpreted as observed semantic state and reference semantic state. Suppose both evolve through `K` with possible per-step semantic source error `eta_n` satisfying:

```text
W_1^{d_sem}(eta_n, nu_n K) <= C_n
```

and:

```text
mu_{n+1} = mu_n K
nu_{n+1} = eta_n
```

Define semantic distortion:

```text
E_n := W_1^{d_sem}(mu_n, nu_n)
```

Then:

```text
E_{n+1} <= delta_sem(K) E_n + C_n
```

If there is no source error (`C_n=0`), semantic distortion contracts by `delta_sem(K)` at each step.

## Proof

By the triangle inequality:

```text
E_{n+1} = W_1(mu_n K, eta_n)
       <= W_1(mu_n K, nu_n K) + W_1(nu_n K, eta_n)
```

The first term is bounded by Theorem 1 and the second term is bounded by `C_n`. Hence:

```text
E_{n+1} <= delta_sem(K) E_n + C_n
```

## Theorem 3 — Holographic semantic stability dichotomy

Assume a uniform source bound:

```text
C_n <= C
```

Then:

1. If `delta_sem(K) < 1`, semantic distortion is dynamically stable:

```text
E_n <= delta_sem(K)^n E_0 + C (1 - delta_sem(K)^n)/(1 - delta_sem(K))
```

and therefore:

```text
limsup_{n -> infinity} E_n <= C / (1 - delta_sem(K))
```

2. If `delta_sem(K) < 1` and `C = 0`, semantic distortion is asymptotically self-correcting:

```text
E_n <= delta_sem(K)^n E_0 -> 0
```

3. If `delta_sem(K) = 1`, the theorem gives marginal stability but no contraction.

4. If `delta_sem(K) > 1`, the theorem gives no semantic stability guarantee.

This is the semantic-tier stability criterion for `HE-PROJ-002` semantic holography.

## Fixture verification — HE-EX-001

`HE-EX-001` has two trace states and kernel:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

With the discrete semantic metric on `{+, -}`:

```text
d_sem(+, -) = 1
```

The total variation distance between the two rows is:

```text
TV([2/3, 1/3], [1/3, 2/3]) = 1/3
```

Therefore:

```text
delta_sem(K) = delta_TV(K) = 1/3
```

The fixture is semantically self-correcting when source error is zero:

```text
E_n <= (1/3)^n E_0
```

## Fixture verification — HE-EX-002

`HE-EX-002` is the continuous phase-flow fixture on `S^1` with two-cell trace and sampling interval `omega Delta t = pi/3`. Its induced two-state kernel is the same:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

Therefore, with the same discrete semantic metric on trace cells:

```text
delta_sem(K) = 1/3
```

and the same semantic self-correction bound applies.

## Task-tier deferral

This theorem is semantic-tier only. It does not prove task distortion stability.

Task distortion requires explicit task primitives:

- action map;
- task loss;
- task-family quantification;
- admissible decision policy.

Those are reserved for `HE-PROJ-TASK-001`. Any future task-tier contraction theorem must cite this document but cannot be inferred from it automatically.

## Boundaries

This document does not derive quantum mechanics. It also does not:

- derive the Born rule;
- assert that semantic stability implies task stability;
- assert that semantic holography implies microstate reconstruction;
- assert that every observed kernel is explanatory;
- solve minimality or identifiability for inverse realizations.

## Citation form

```text
[HE-PROJ-003 @ <merge-sha>]
[HE-PROJ-001 @ e57f8f386c412ff68283783d3e7142bef81503d9]
[HE-PROJ-002 @ 2c8cb6b7cd4629adbf68d063e83dd15835a80360]
[HE-PROJ-INV-001 @ b8cd01ad53ed71392a0f47b7041dbde143ed11dd]
[A-HE-PROJ-004 @ <merge-sha>]
```

## Versioning

This is `HE-PROJ-003 v1.0`. Any extension to task-tier distortion requires a new theorem or a major version update after `HE-PROJ-TASK-001` is active.
