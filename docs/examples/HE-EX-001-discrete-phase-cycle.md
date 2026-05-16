# HE-EX-001 — Discrete Phase Cycle Fixture

Identifier: `HE-EX-001`  
Status: active after this PR  
Anti-seed: `A-HE-EX-001`, `A-HE-PROJ-001`

## Construction

Let:

```text
X = Z_12
f(x) = x + 2 mod 12
Y = {+, -}
```

Define trace map `tau : X -> Y` by the fibers:

```text
F_+ = {11, 0, 1, 2, 3, 4}
F_- = {5, 6, 7, 8, 9, 10}
```

Use uniform measures on each fiber.

## Kernel computation

Starting from `+`:

```text
11 -> 1  -> +
0  -> 2  -> +
1  -> 3  -> +
2  -> 4  -> +
3  -> 5  -> -
4  -> 6  -> -
```

Thus:

```text
K(+, +) = 4/6 = 2/3
K(+, -) = 2/6 = 1/3
```

Starting from `-`:

```text
5  -> 7  -> -
6  -> 8  -> -
7  -> 9  -> -
8  -> 10 -> -
9  -> 11 -> +
10 -> 0  -> +
```

Thus:

```text
K(-, +) = 2/6 = 1/3
K(-, -) = 4/6 = 2/3
```

The induced kernel is:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

with row order `+, -` and column order `+, -`.

## Information quantities

For the uniform distribution on `X`:

```text
H(X) = log2(12)
H(Y) = 1
H(X | Y) = log2(6)
```

The trace loses `log2(6)` bits of microstate information while preserving a two-state interface.

## Role

This fixture validates `HE-PROJ-001` on a finite deterministic system with a many-to-one trace. The latent evolution is deterministic; the observer-level law is stochastic because the next trace varies across each fiber.

## Boundary

This is fixture-grade. It does not derive quantum mechanics, the Born rule, measurement theory, or any physical prediction.
