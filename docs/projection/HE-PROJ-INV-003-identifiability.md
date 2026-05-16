# HE-PROJ-INV-003 — Identifiability of the Latent Substrate

**Identifier:** `HE-PROJ-INV-003`  
**Status:** active  
**Parents:** `HE-PROJ-001` (induced kernel), `HE-PROJ-INV-001` (realizability / existence)  
**Companion-reserved:** `HE-PROJ-INV-002` (minimality — remains reserved)  
**Scope:** finite trace space `Y`  
**Canonical-source:** authored from framework principles; classical ergodic-theory backing (Rokhlin natural extension, Kolmogorov extension theorem)  
**Anti-seed:** `A-HE-PROJ-003`, `A-HE-PROJ-005`

## Position in the inverse-problem package

`HE-PROJ-001` established the forward map: a substrate triple `(X, f, tau)` with global measure `mu` induces a Markov kernel `K` on `Y`.

`HE-PROJ-INV-001` proved **existence**: every countable Markov kernel admits a deterministic realization, via the skew product `X = Y x [0,1)`.

This document addresses **identifiability**: the latent substrate is not unique, but it becomes unique once restricted to a natural class. The two-sided Markov shift is the canonical representative of that class. The skew product is hereby demoted to *a* realization — not the canonical one.

The third subproblem, **minimality** (`HE-PROJ-INV-002`), remains reserved and genuinely open. See `Relation to HE-PROJ-INV-002` below for why identifiability and minimality optimize different objects and do not collide.

## Scope

This document treats **finite `Y`**. For finite `Y` a stationary law always exists, and the uniqueness theorem is unconditional.

The countably-infinite case — where a kernel may have no stationary probability measure (transient or null-recurrent chains) — introduces genuine ergodic-theory subtlety (infinite-measure-preserving natural extensions, sigma-finite constructions, Krieger-type constructions). It is reserved as `HE-PROJ-INV-003-COUNTABLE`.

## The non-uniqueness that motivates the theorem

The skew-product realization of `HE-PROJ-INV-001` is not unique even up to isomorphism.

Fix a kernel `K` on `Y`. The skew product:

```text
X = Y x [0,1)
tau(y,s) = y
```

with `f` defined by partitioning each fiber `[0,1)` into intervals of length `K(y,y')` and mapping affinely admits a continuum of internally distinct variants. Any measure-preserving rearrangement of the `[0,1)` factor — permuting target intervals or composing with a measure-preserving automorphism of `[0,1)` — yields a different triple `(X, f, tau)` inducing the same `K`.

So “which latent substrate produced `K`” is radically underdetermined by `K` alone. Identifiability is therefore not a uniqueness statement about realizations in general. It is a uniqueness statement **relative to a class of realizations**, and the content of the theorem is the choice of class.

## The canonical realization: two-sided Markov shift

Let `K` be a Markov kernel on a finite set `Y`. A stationary law `nu` — a probability vector with:

```text
nu K = nu
```

exists by the finite Markov-chain stationary-measure theorem.

Define:

```text
X = Y^Z
f : X -> X,      (f omega)_n = omega_{n+1}      # left shift
tau : X -> Y,    tau(omega) = omega_0
```

Let `mu_K` be the **two-sided Markov measure** on `Y^Z` determined by `nu` and `K`: the unique shift-invariant probability measure whose one-dimensional marginal is `nu` and whose two-step conditional law is `K`.

Concretely, on a cylinder fixing coordinates `m <= n`:

```text
mu_K({omega : omega_m = y_m, ..., omega_n = y_n})
  = nu(y_m) product_{j=m}^{n-1} K(y_j, y_{j+1})
```

## Existence of the two-sided Markov measure

The finite-dimensional cylinder probabilities above are consistent.

- Marginalizing the right endpoint uses row stochasticity:

```text
sum_{y_{n+1}} K(y_n, y_{n+1}) = 1
```

- Marginalizing the left endpoint uses stationarity:

```text
nu K = nu
```

By the Kolmogorov extension theorem, a unique probability measure `mu_K` on `Y^Z` with these finite-dimensional marginals exists. The one-sided analogue on `Y^N` is the Ionescu-Tulcea construction; the two-sided case additionally uses stationarity to extend consistently into negative coordinates.

The shift `f` is a bijection of `Y^Z`; `mu_K` is shift-invariant by stationarity. Hence `f` is invertible and `mu_K`-preserving.

## Induced-kernel check

Since:

```text
tau(f omega) = (f omega)_0 = omega_1
```

and the fiber:

```text
F_y = {omega : omega_0 = y}
```

carries the conditional measure `mu_y = mu_K(. | omega_0 = y)`, we have:

```text
mu_y({omega : omega_1 = y'}) = P_mu_K[omega_1 = y' | omega_0 = y] = K(y,y')
```

Therefore the induced kernel of `(Y^Z, f, tau, mu_K)` is exactly `K`.

Unlike the skew product, this realization is **intrinsic** — constructed from `Y`, `K`, and stationary law `nu` alone, with no arbitrary `[0,1)` factor — **measure-preserving**, **stationary**, and **invertible**.

## The tau-generation condition

**Definition (`tau`-generated realization).** A realization `(X, f, tau, mu)` is `tau`-generated if the smallest `f`-invariant sub-sigma-algebra of `B_X` containing `tau^{-1}(B_Y)` equals `B_X` modulo `mu`-null sets:

```text
vee_{n in Z} f^{-n}(tau^{-1}(B_Y)) = B_X   mod mu
```

Equivalently: the trace observable `tau` together with all its dynamical translates `tau o f^n` separates points of `X` almost everywhere. There is no bulk structure invisible to the observer across all time.

The skew product fails this condition: the `[0,1)` coordinate is not recoverable from the trace history `(tau(f^n x))_{n in Z}`. The trace history sees which interval a point occupies at each step, not the point’s position inside invisible substructure. The `[0,1)` factor is hidden bulk structure.

## Theorem — Identifiability

Let `K` be a Markov kernel on a finite set `Y`. Among all realizations `(X, f, tau, mu)` of `K` that are:

1. **invertible** — `f` is a bimeasurable bijection mod null;
2. **measure-preserving** — `f_* mu = mu`;
3. **stationary** — `tau_* mu = nu`, a stationary law of `K`;
4. **tau-generated** — the trace history generates the full sigma-algebra mod null;

the two-sided Markov shift `(Y^Z, shift, coordinate_0, mu_K)` is **unique up to measure-theoretic isomorphism**.

Equivalently: any two realizations satisfying (1)–(4) are conjugate by an a.e.-defined bijection `Psi` intertwining the dynamics and the trace maps:

```text
Psi o f = f' o Psi
tau' o Psi = tau
```

## Proof

Let `(X, f, tau, mu)` satisfy (1)–(4). Define the coding map:

```text
Phi : X -> Y^Z
Phi(x) = (tau(f^n x))_{n in Z}
```

`Phi` is measurable because each coordinate map `x -> tau(f^n x)` is measurable.

For every `n`:

```text
Phi(fx)_n = tau(f^n(fx)) = tau(f^{n+1}x) = Phi(x)_{n+1} = (shift Phi(x))_n
```

so `Phi o f = shift o Phi`. Also `(coordinate_0 o Phi)(x) = tau(x)`.

`Phi_* mu` is shift-invariant because `mu` is `f`-invariant and `Phi` intertwines `f` with the shift. Its one-dimensional marginal is `tau_* mu = nu` by stationarity. Its two-step conditional law is:

```text
P_{Phi_*mu}[omega_1 = y' | omega_0 = y]
  = mu_y({x : tau(fx) = y'})
  = K(y,y')
```

because `(X, f, tau, mu)` realizes `K`.

Therefore every finite cylinder under `Phi_* mu` has the Markov cylinder probability:

```text
nu(y_m) product_{j=m}^{n-1} K(y_j, y_{j+1})
```

By Kolmogorov uniqueness, `Phi_* mu = mu_K`.

If `Phi(x) = Phi(x')`, then `tau(f^n x) = tau(f^n x')` for all `n in Z`. By tau-generation, the sigma-algebra generated by all trace coordinates is all of `B_X` mod null. Thus `Phi` is injective mod null.

`Phi` is a measurable injection between standard Borel probability spaces with pushforward `mu_K`. By the Lusin-Souslin theorem, its image is measurable and `Phi` is a Borel isomorphism onto its image. Since `Phi_* mu = mu_K`, the image has full `mu_K` measure.

Thus `Phi` is a measure-theoretic isomorphism mod null, intertwining dynamics and trace. This proves the theorem.

## Sharpness: each hypothesis is load-bearing

The theorem is uniqueness relative to the class (1)–(4). Dropping any single hypothesis breaks uniqueness.

### Drop tau-generation

The skew product `X = Y x [0,1)` realizes `K`, can be made invertible, measure-preserving, and stationary, but is not tau-generated. It carries an extra `[0,1)` factor invisible to `tau`. Non-unique.

### Drop invertibility

The one-sided Markov shift `(Y^N, shift, coordinate_0, mu_K^+)` realizes `K`, is measure-preserving, stationary, and tau-generated, but it is not invertible. It is not isomorphic to the two-sided shift as a measure-preserving dynamical system. Non-unique.

### Drop stationarity

A non-stationary Markov measure can induce the same one-step kernel `K` but a different path measure. Stationarity is required for the canonical two-sided invariant measure. Non-unique.

### Drop measure preservation

A dissipative realization can induce the prescribed conditional kernel `K` locally while the global measure and kernel decouple. Non-unique.

## Interpretation

The latent substrate of a projection-induced Markov kernel is **not unique**. `HE-PROJ-INV-001` already showed many realizations exist.

`HE-PROJ-INV-003` establishes that the non-uniqueness is resolved by four natural requirements. The canonical representative selected by those requirements is the two-sided Markov shift — the Rokhlin natural extension of the one-sided Markov system.

This is a uniqueness theorem with four qualifiers. It is not a claim that the substrate is metaphysically determined. Per `A-HE-PROJ-003`, universal realizability is not explanation. Per `A-HE-PROJ-005`, the canonical Markov shift is not physical substrate uniqueness.

## Demotion of the skew product

`HE-PROJ-INV-001`'s skew product `X = Y x [0,1)` is hereby recorded as **a realization, not the canonical realization**.

Its role is existence-of-some-realization. The canonical realization for identifiability and structural purposes is the two-sided Markov shift of this document.

`HE-PROJ-INV-001`'s existence claim is unaffected and stands. This PR also adds a forward cross-reference to the `HE-PROJ-INV-001` document.

## Relation to HE-PROJ-INV-002

`HE-PROJ-INV-002` asks for the *smallest* realization — the finite-state complexity functional `cx(K) = inf |X|` over finite realizations. `HE-PROJ-INV-003` and `HE-PROJ-INV-002` optimize different objects and do not collide:

- INV-003's canonical realization is infinite: `X = Y^Z`.
- INV-003 is canonical with respect to invertibility, stationarity, and tau-generation.
- INV-002's minimal realization is finite, with no invertibility requirement.

So a kernel can have a canonical invertible stationary realization and a distinct finite minimal realization without contradiction.

`HE-PROJ-INV-002` remains reserved and genuinely open: the structure of `cx(K)`, its computability, its behavior under kernel composition, and its relation to matrix rank or nonnegative rank remain unresolved.

## Fixture: HE-EX-001 canonical realization

`HE-EX-001` is the kernel:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

on `Y = {+, -}`. The stationary law is `nu = (1/2, 1/2)`. The canonical realization is the two-sided Markov shift on `{+, -}^Z` with Markov measure determined by `nu` and `K`.

The Kolmogorov-Sinai entropy rate is:

```text
h(mu_K) = - sum_y nu(y) sum_{y'} K(y,y') log_2 K(y,y')
```

For this symmetric two-state chain:

```text
h(mu_K) = - (2/3) log_2(2/3) - (1/3) log_2(1/3)
        = log_2 3 - 2/3
        ≈ 0.918295834 bits / step
```

`HE-EX-001`'s stated `Z_12` realization is a finite periodic orbit and therefore has entropy zero. The same kernel has two different dynamical realizations: finite/periodic/zero-entropy versus infinite/stationary/observer-generated/positive-entropy.

## Countable extension reservation

This document proves finite `Y` only.

`HE-PROJ-INV-003-COUNTABLE` is reserved for countably-infinite `Y`. The countable case may require stationarity hypotheses, sigma-finite measures, infinite-measure-preserving natural extensions, or non-stationary extensions. No countable-state theorem is active in this PR.

## What this document does not do

This document does not:

- claim the latent substrate is metaphysically unique;
- solve minimality (`HE-PROJ-INV-002` remains reserved and open);
- treat countably-infinite `Y` (`HE-PROJ-INV-003-COUNTABLE` is reserved);
- treat non-stationary or dissipative realizations except as sharpness counterexamples;
- derive quantum mechanics;
- derive the Born rule;
- derive noncommuting observables or entanglement;
- assert physical instantiation of the canonical realization;
- transfer methodology to constitute proof of any Clay-program claim.

## Canonical citation form

```text
[HE-PROJ-INV-003 @ <merge-sha>]
[A-HE-PROJ-005 @ <merge-sha>]
```

Cross-citations:

```text
[HE-PROJ-001 @ e57f8f386c412ff68283783d3e7142bef81503d9]
[HE-PROJ-INV-001 @ b8cd01ad53ed71392a0f47b7041dbde143ed11dd]
[A-HE-PROJ-003 @ b8cd01ad53ed71392a0f47b7041dbde143ed11dd]
[HE-EX-001 @ e57f8f386c412ff68283783d3e7142bef81503d9]
```

Bibliographic references:

```text
Rokhlin, V. A. (1961). Exact endomorphisms of a Lebesgue space — natural extension.
Kolmogorov extension theorem — Markov measure on the product.
Ionescu-Tulcea theorem — one-sided Markov construction.
Heller, M. D. (2026). Temporal Mechanics and Emergence v0.24.1, Section 11 — image/preimage discipline.
```
