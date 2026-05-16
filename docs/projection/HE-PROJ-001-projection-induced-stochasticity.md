# HE-PROJ-001 — Projection-Induced Stochasticity Theorem

Identifier: `HE-PROJ-001`  
Distance tier: framework-method / theorem-specification  
Status: active after this PR  
Anti-seed: `A-HE-PROJ-001`, `A-HE-PROJ-002`, `A-HE-MTH-001`

## Statement

Let `X` and `Y` be measurable spaces. Let:

```text
f : X -> X
```

be deterministic measurable dynamics, and let:

```text
tau : X -> Y
```

be a measurable surjective trace map. For each `y in Y`, define the fiber:

```text
F_y := tau^{-1}(y)
```

Let `mu_y` be a probability measure supported on `F_y`. Define:

```text
K(y, B) := mu_y({x in F_y : tau(f(x)) in B})
```

for measurable `B subseteq Y`.

Then `K` is a Markov kernel from `Y` to `Y`.

If `Y` is finite or countable, this specializes to:

```text
K(y, y') := mu_y({x in F_y : tau(f(x)) = y'})
```

## Proof

For fixed `y`, the map:

```text
x |-> tau(f(x))
```

is measurable because `f` and `tau` are measurable. Therefore the set:

```text
{x in F_y : tau(f(x)) in B}
```

is measurable in `F_y` for each measurable `B subseteq Y`. Since `mu_y` is a probability measure on `F_y`, the function:

```text
B |-> K(y, B)
```

is a probability measure on `Y`.

For fixed `B`, measurability of:

```text
y |-> K(y, B)
```

is assumed as part of the measurable family condition on `{mu_y}`. Therefore `K` is a Markov kernel.

## Deterministic criterion

The induced observer-level kernel is deterministic at `y` iff there exists `y* in Y` such that:

```text
K(y, {y*}) = 1
```

Equivalently, `tau o f` is `mu_y`-almost surely constant on `F_y`.

If there exist `y'_1 != y'_2` such that both:

```text
mu_y({x in F_y : tau(f(x)) = y'_1}) > 0
mu_y({x in F_y : tau(f(x)) = y'_2}) > 0
```

then the observer-level transition law is stochastic at `y`.

## Interpretation

Deterministic latent dynamics can induce stochastic observer-level laws when the trace map is many-to-one and the next trace is not constant across the fiber.

The stochasticity is projection-induced. It reflects information discarded by the trace map, not indeterminism in the latent dynamics.

## Parent-document framing

Temporal Mechanics v0.24.1 imports the same image / preimage and projection discipline at substrate level. The relevant parent formulation is bibliographic rather than repo-pinned:

```text
Heller, Michael D. Temporal Mechanics and Emergence, v0.24.1 reconstructed editable source, 2026-05-08, §§11-12.
```

That manuscript-level reference remains bibliographic. This repository canonicalizes the HE-PROJ theorem surface.

## Heller-Dirac structural cognate

`HD-FND-007` gives the Tomita-Takesaki modular operator and modular flow. HE-PROJ-001 does not use modular flow in its proof. The relation is structural-cognate only:

- HD-FND-007: state-dependent automorphism flow on an algebra of observables.
- HE-PROJ-001: trace-map-induced Markov kernel on observer-level traces.

Both organize time-like or evolution structure on observer-accessible data, but neither proves the other.

Per `A-HD-TM-001`, modular flow is not automatically physical time. Per `A-HE-MTH-001`, the cognate relationship is method-grade only.

## Boundaries

This theorem does not derive quantum mechanics. It also does not:

- derive the Born rule;
- produce noncommuting observables;
- produce Hilbert-space measurement theory;
- produce entanglement;
- claim that all physical probability is projection-induced;
- assert that semantic lift is observer-independent;
- collapse ontology to boundary traces.

It proves a narrower statement: many-to-one observation of deterministic dynamics induces a Markov kernel, generically stochastic when the next trace varies across fibers.

## Canonical exemplars

This PR also activates:

- `HE-EX-001` — discrete phase cycle on `Z_12`;
- `HE-EX-002` — continuous phase flow on `S^1`.

Both recover the kernel:

```text
[[2/3, 1/3], [1/3, 2/3]]
```

They are fixtures, not physical predictions.

## Inverse-problem reservation

This theorem naturally raises an inverse problem: given a Markov kernel `K` on `Y`, characterize deterministic latent systems `(X, f, tau, mu_y)` that realize `K` up to equivalence.

The inverse problem is reserved under `HE-PROJ-INV-001` for a future PR. It is not solved here.
