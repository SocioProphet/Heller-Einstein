# Projection-Induced Stochasticity

Status: canonical Heller-Einstein v0.1 theorem surface.  
Source: Einstein-Heller Interface Program v1.7 verified source candidate.  
Identifier: `HE-PROJ-001`.  
Claim level: theorem-grade under stated typed-interface assumptions.

## Purpose

This document records the projection-induced stochasticity theorem from the v1.7 Einstein-Heller source candidate.

The theorem is the technical Einstein-direction result: deterministic latent evolution, observed through a many-to-one trace map with fiber measures, induces an observer-level Markov kernel that is deterministic exactly when the projected successor is almost surely fiber-constant.

It is not a derivation of quantum mechanics.

## HE-PROJ-001 — Projection-induced stochasticity theorem

Let:

```text
f : X -> X
```

be deterministic and let:

```text
tau : X -> Y
```

be surjective.

For each `y in Y`, define the compatible latent fiber:

```text
F_y := tau^{-1}(y)
```

Let `mu_y` be a probability measure supported on `F_y`.

Define:

```text
K(y, y') := mu_y({x in F_y : tau(f(x)) = y'})
```

Then `K` is a Markov kernel on `Y`.

Moreover, `K` is deterministic iff:

```text
tau o f
```

is `mu_y`-almost surely constant on each fiber `F_y`. Otherwise the observer-level induced law is stochastic.

## Proof outline

For fixed `y`, set:

```text
A_y' := {x in F_y : tau(f(x)) = y'}
```

The sets `A_y'` are measurable, pairwise disjoint, and their union is `F_y`.

Therefore:

```text
K(y, y') = mu_y(A_y') >= 0
```

and:

```text
sum_y' K(y, y') = sum_y' mu_y(A_y') = mu_y(F_y) = 1
```

So `K` is a Markov kernel.

If `tau o f` is almost surely constant on `F_y`, then exactly one projected successor has probability `1`.

If two distinct projected futures occur on positive-measure subsets of `F_y`, the induced transition is nontrivial and stochastic.

## HE-EX-001 — Discrete phase-cycle exemplar

Grade: fixture-grade exemplar.

Let:

```text
X = Z_12
f(x) = x + 2 mod 12
Y = {+, -}
F_+ = {11, 0, 1, 2, 3, 4}
F_- = {5, 6, 7, 8, 9, 10}
```

With uniform measures on each fiber, the induced kernel is:

```text
K = [[2/3, 1/3],
     [1/3, 2/3]]
```

Information quantities:

```text
H(X) = log_2 12 ~= 3.585
H(Y) = 1
H(X | Y) = log_2 6 ~= 2.585
```

## HE-EX-002 — Continuous phase-flow exemplar

Grade: fixture-grade exemplar.

Let:

```text
X = S^1 = R / 2 pi Z
theta(t) = theta_0 + omega t mod 2 pi
```

For a two-cell trace partition and sampling interval:

```text
omega Delta t = pi / 3
```

the same kernel appears:

```text
K = [[2/3, 1/3],
     [1/3, 2/3]]
```

## Scope of validity

The theorem assumes:

1. deterministic latent dynamics `f : X -> X`;
2. a surjective trace map `tau : X -> Y`;
3. measurable fibers `F_y`;
4. probability measures `mu_y` supported on each fiber;
5. the induced successor event sets are measurable.

The stochasticity is projection-induced at the observer trace level. It is not a claim that latent dynamics are intrinsically stochastic.

## Non-claims

`HE-PROJ-001` does not derive quantum mechanics.

`HE-PROJ-001` does not derive the Born rule.

`HE-PROJ-001` does not derive noncommuting observables.

`HE-PROJ-001` does not derive entanglement structure.

`HE-PROJ-001` does not identify the correct latent state space for any physical theory.

`HE-PROJ-001` does not prove that any particular observed stochastic law is explained by a specific latent deterministic substrate.

`HE-PROJ-001` does not transfer proof content into Heller-Godel, Heller-Dirac, Yang-Mills, or any other downstream repository.
