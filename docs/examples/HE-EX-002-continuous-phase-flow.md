# HE-EX-002 — Continuous Phase Flow Fixture

Identifier: `HE-EX-002`  
Status: active after this PR  
Anti-seed: `A-HE-EX-001`, `A-HE-PROJ-001`

## Construction

Let:

```text
X = S^1 = R / 2pi Z
```

with deterministic flow:

```text
theta(t + Delta t) = theta(t) + omega Delta t mod 2pi
```

Set:

```text
omega Delta t = pi / 3
```

Partition `S^1` into two semicircle trace cells:

```text
Y = {+, -}
F_+ = [-pi/2, pi/2)
F_- = [pi/2, 3pi/2)
```

with normalized Lebesgue measure on each fiber.

## Kernel computation

A rotation by `pi/3` moves one third of each semicircle across the boundary and leaves two thirds in the same trace cell.

Thus:

```text
K(+, +) = 2/3
K(+, -) = 1/3
K(-, +) = 1/3
K(-, -) = 2/3
```

The induced kernel is:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

with row order `+, -` and column order `+, -`.

## Relation to HE-EX-001

`HE-EX-001` gives the finite cyclic realization on `Z_12`. This fixture gives the continuous phase-flow realization on `S^1`. Both validate `HE-PROJ-001` by producing the same observer-level kernel from deterministic latent dynamics and many-to-one trace.

## Boundary

This is fixture-grade. It does not derive quantum mechanics, the Born rule, continuous measurement theory, or any physical prediction.
