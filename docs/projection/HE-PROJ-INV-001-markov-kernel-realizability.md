# HE-PROJ-INV-001 — Markov Kernel Realizability Theorem

Identifier: `HE-PROJ-INV-001`  
Parent theorem: `HE-PROJ-001`  
Parent interface ontology: `HE-INT-001`  
Status: active after this PR  
Claim grade: theorem-grade within the stated measurable / countable setting  
Anti-seed: `A-HE-PROJ-001`, `A-HE-PROJ-003`

## Problem

`HE-PROJ-001` gives the forward construction:

```text
substrate quadruple (X, f, tau, {mu_y}) -> induced Markov kernel K
```

where:

- `X` is the latent state space;
- `f : X -> X` is deterministic dynamics;
- `tau : X -> Y` is a surjective trace map;
- `F_y := tau^{-1}(y)` is the trace fiber;
- `mu_y` is a probability measure supported on `F_y`;
- `K(y, B) = mu_y({x in F_y : tau(f(x)) in B})`.

The inverse problem asks what can be recovered from an observed kernel `K`.

This document solves the first inverse subproblem: existence / realizability.

## Theorem 1 — Countable Markov kernels are deterministically realizable

Let `Y` be a countable set and let `K : Y x Y -> [0,1]` be a Markov kernel:

```text
sum_{y' in Y} K(y, y') = 1
```

for every `y in Y`.

Then there exists a substrate quadruple:

```text
(X, f, tau, {mu_y}_{y in Y})
```

such that the kernel induced by `HE-PROJ-001` is exactly `K`.

## Construction

Let:

```text
X = Y x [0,1)
tau(y, s) = y
F_y = {y} x [0,1)
mu_y = delta_y tensor Lebesgue_[0,1)
```

For each `y in Y`, choose an enumeration of `Y`:

```text
Y = {y'_0, y'_1, y'_2, ...}
```

adapted to the row `K(y, -)`. Define cumulative weights:

```text
a_0(y) = 0
a_{n+1}(y) = a_n(y) + K(y, y'_n)
```

and intervals:

```text
I_{y -> y'_n} = [a_n(y), a_{n+1}(y))
```

with the convention that zero-length intervals are ignored.

For `s in I_{y -> y'_n}`, define:

```text
f(y, s) = (y'_n, g_{y,n}(s))
```

where `g_{y,n}` is any measurable map from `I_{y -> y'_n}` into `[0,1)`. If `K(y, y'_n) > 0`, one convenient choice is the affine rescaling:

```text
g_{y,n}(s) = (s - a_n(y)) / K(y, y'_n)
```

For zero-length intervals, no definition is needed on that interval.

## Proof

For any `y, y' in Y`, the induced kernel is:

```text
K_ind(y, y') = mu_y({(y, s) in F_y : tau(f(y, s)) = y'})
```

By construction, `tau(f(y, s)) = y'` exactly when `s` lies in the union of intervals assigned to `y'`. Since the row construction assigns interval length `K(y, y')`, we get:

```text
K_ind(y, y') = Lebesgue(I_{y -> y'}) = K(y, y')
```

for every `y, y'`. Therefore `K_ind = K`.

The map `f` is measurable because it is piecewise measurable on the countable measurable partition of each fiber. Thus the constructed quadruple is admissible and realizes `K`.

This proves the theorem.

## Corollary 1 — Realizability is universal

Every countable Markov dynamics admits a deterministic latent realization through a many-to-one trace map.

Equivalently: from the existence of an observed Markov kernel alone, one cannot rule out deterministic substrate dynamics.

## Anti-interpretation corollary — Universal realizability is not explanation

Theorem 1 is a universality result, not an explanatory result. Since every countable Markov kernel is realizable, deterministic-substrate existence alone explains no special structure of the observed kernel.

Explanatory weight requires additional constraints, such as:

- minimal latent space;
- canonical fiber measures;
- identifiability of realization class;
- compatibility with additional physical, semantic, or task structure;
- compositionality under kernel composition.

This is the purpose of the reserved inverse subproblems `HE-PROJ-INV-002` and `HE-PROJ-INV-003`.

## Supporting proposition — finite uniform rational realization

Let `Y` be finite and suppose all entries of `K` are rational. Let `D_y` be a common denominator for the row `{K(y, y')}_{y' in Y}`. Then `K` admits a finite uniform-fiber realization with:

```text
|F_y| = D_y
```

for each `y`, using exactly `D_y K(y, y')` points in `F_y` that map to target trace `y'`.

If a single common denominator `D` is used for all rows, then a finite uniform realization exists with:

```text
|X| = |Y| D
```

## Supporting proposition — irrational obstruction for finite uniform fibers

If a finite uniform-fiber realization exists, then every kernel entry is rational. Specifically, if `|F_y| = n_y` and `mu_y` is uniform on `F_y`, then:

```text
K(y, y') = m_{y,y'} / n_y
```

for some integer `m_{y,y'}`.

Therefore any kernel with an irrational entry admits no finite uniform-fiber realization. It can still be realized by Theorem 1 using `[0,1)` fibers, or by a finite realization with non-uniform fiber measures if allowed.

## Worked minimality observation — HE-EX-001 is not finite-minimal

`HE-EX-001` realizes the two-state kernel:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

using `X = Z_12`, with two trace fibers each of size 6.

A smaller finite uniform realization exists with two fibers of size 3:

```text
X_min = {+, -} x {0,1,2}
```

with uniform measure on each fiber.

Define deterministic dynamics by sending, in each fiber, two states to the same trace and one state to the opposite trace:

```text
(+ ,0) -> (+,0)
(+ ,1) -> (+,1)
(+ ,2) -> (-,0)
(- ,0) -> (-,0)
(- ,1) -> (-,1)
(- ,2) -> (+,0)
```

with trace map `tau(sign, i) = sign`. This realizes the same kernel with:

```text
|X_min| = 6
```

Thus the `Z_12` fixture is realizable and useful pedagogically, but not finite-minimal.

This observation is included here as a supporting result. It does not activate the full minimality problem.

## Reserved subproblem — HE-PROJ-INV-002 minimality

`HE-PROJ-INV-002` is reserved for the minimality problem.

For a finite kernel `K`, define:

```text
m(K) = min |X|
```

among finite realizing substrate quadruples under a declared class of allowed fiber measures, with `m(K) = infinity` if none exists.

Open questions include:

1. For which allowed-measure classes is `m(K)` computable?
2. How does `m(K)` behave under kernel composition?
3. Is `m(K)` submultiplicative, additive, or neither under products?
4. How does `m(K)` relate to matrix rank, nonnegative rank, or stochastic factorization rank?
5. What additional constraints make the minimal realization canonical?

This PR does not solve `HE-PROJ-INV-002`.

## Reserved subproblem — HE-PROJ-INV-003 identifiability

`HE-PROJ-INV-003` is reserved for identifiability.

Two substrate quadruples are kernel-equivalent if they induce the same kernel `K` on `Y`.

A necessary source of non-identifiability is fiberwise measure rearrangement: if `h_y : F_y -> F_y` is a measure-preserving automorphism on each fiber, then conjugating the latent dynamics by the `h_y` changes the internal substrate dynamics while leaving the induced kernel unchanged.

Therefore the kernel sees only the distribution of target traces under `tau o f` on each fiber, not the internal arrangement of latent states inside the fiber.

Open questions include:

1. What equivalence relation on substrate quadruples is the correct one for identifiability?
2. Is fiberwise measure-isomorphism plus pushdown compatibility sufficient for kernel-equivalence?
3. What additional structure — topology, metric, semantics, task loss, or dynamics class — restores identifiability?
4. Is there a canonical minimal representative in each kernel-equivalence class?

This PR does not solve `HE-PROJ-INV-003`.

## Relationship to Temporal Mechanics v0.24.1

Temporal Mechanics v0.24.1 frames the image / preimage discipline at substrate level. `HE-PROJ-INV-001` is the inverse side of that same discipline: it asks what latent preimage systems can realize a given observed image-level transition law.

Citation remains bibliographic:

```text
Heller, Michael D. Temporal Mechanics and Emergence, v0.24.1 reconstructed editable source, 2026-05-08, Section 11.
```

## Relationship to HE-PROJ-001

`HE-PROJ-001` proves the forward construction. `HE-PROJ-INV-001` proves the total existence inverse theorem for countable kernels.

Forward:

```text
(X, f, tau, mu_y) -> K
```

Inverse existence:

```text
K -> some (X, f, tau, mu_y)
```

The inverse is not unique and not explanatory without extra constraints.

## Boundaries

This document does not derive quantum mechanics. It also does not:

- derive the Born rule;
- prove that physical probability is projection-induced;
- explain why a particular physical kernel has its observed form;
- solve the minimality problem;
- solve the identifiability problem;
- assert a unique latent substrate;
- make claims about Hilbert spaces, observables, or entanglement.

## Citation form

```text
[HE-PROJ-INV-001 @ <merge-sha>]
[A-HE-PROJ-003 @ <merge-sha>]
[HE-PROJ-001 @ e57f8f386c412ff68283783d3e7142bef81503d9]
[HE-INT-001 @ 59d41f8d7691937322355f1ab57243884ad81a1c]
```

## Versioning

This is `HE-PROJ-INV-001 v1.0`. Future PRs may extend the theorem to general measurable spaces, Polish spaces, or constrained substrate classes. Those extensions require explicit theorem statements and proofs.
