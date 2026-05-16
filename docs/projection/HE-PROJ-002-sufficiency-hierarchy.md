# HE-PROJ-002 — Sufficiency Hierarchy and Semantic Holography

Identifier: `HE-PROJ-002`  
Parent interface ontology: `HE-INT-001`  
Depends on: `HE-PROJ-001`, `HE-EX-001`  
Distance tier: framework-method / theorem-specification  
Status: active after this PR  
Anti-seed: `A-HE-PROJ-002`, `A-HE-INT-001`, `A-HE-INT-002`, `A-HE-EX-001`

## Scope

This document formalizes the Heller-Einstein sufficiency hierarchy:

1. microstate sufficiency;
2. semantic sufficiency;
3. task sufficiency;
4. semantic holography as low semantic distortion below full microstate rate.

This is a Tier B formalization: it proves microstate sufficiency implies semantic sufficiency, gives an explicit counterexample to the converse using `HE-EX-001`, and adds a rate-distortion framing. It does not formalize the task-sufficiency lattice; that is reserved under `HE-PROJ-TASK-001`.

## Setup

Use the interface vocabulary of `HE-INT-001`:

```text
X --tau_O--> Y_O --S_O--> M_O
```

where:

- `X` is latent / bulk state space;
- `Y_O` is observer trace space;
- `tau_O : X -> Y_O` is the trace map;
- `S_O : Y_O -> M_O` is the observer-relative semantic lift;
- `R_O : Y_O -> X` is a reconstruction map when available.

Assume distance functions or losses:

```text
d_X : X x X -> R_{0}
d_M : M_O x M_O -> R_{0}
```

where the exact regularity assumptions are domain-specific. Metric, pseudometric, or loss-function variants are allowed when declared.

Let `U subseteq X` be a declared evaluation domain.

## Pointwise reconstruction error

For `x in U`, define pointwise reconstruction error:

```text
epsilon_rec^O(x) := d_X(x, R_O(tau_O(x)))
```

This measures microstate reconstruction error after tracing and reconstructing.

## Strong microstate sufficiency

The interface is strongly microstate sufficient on `U` iff:

```text
R_O o tau_O = id_U
```

Equivalently:

```text
epsilon_rec^O(x) = 0 for all x in U
```

Microstate sufficiency means the trace carries enough information to reconstruct the latent state on `U`.

## Semantic distortion

For `x in U`, define semantic distortion:

```text
delta_sem^O(x) := d_M(S_O(tau_O(x)), S_O(tau_O(R_O(tau_O(x)))))
```

This measures whether the reconstructed representative preserves the observer-relative meaning of the original trace.

## Semantic sufficiency

The interface is semantically sufficient on `U` iff:

```text
S_O o tau_O o R_O o tau_O = S_O o tau_O on U
```

Equivalently:

```text
delta_sem^O(x) = 0 for all x in U
```

Semantic sufficiency means the trace/reconstruction loop may lose microstate information while preserving observer-relative meaning.

## Task sufficiency

Let a task be specified by an action or decision map:

```text
A_O : M_O -> Z_O
```

and a task loss:

```text
L_task : Z_O x Z_O -> R_{0}
```

The interface is task sufficient for `(A_O, L_task)` on `U` iff:

```text
L_task(A_O(S_O(tau_O(x))), A_O(S_O(tau_O(R_O(tau_O(x)))))) = 0
```

for all `x in U`.

Task sufficiency is weaker and task-relative. The lattice of task-sufficiency relations is not formalized here; it is reserved under `HE-PROJ-TASK-001`.

## Theorem: microstate sufficiency implies semantic sufficiency

If an interface is strongly microstate sufficient on `U`, then it is semantically sufficient on `U`.

### Proof

Assume strong microstate sufficiency on `U`:

```text
R_O(tau_O(x)) = x
```

for all `x in U`. Apply `tau_O` to both sides:

```text
tau_O(R_O(tau_O(x))) = tau_O(x)
```

Apply `S_O` to both sides:

```text
S_O(tau_O(R_O(tau_O(x)))) = S_O(tau_O(x))
```

Therefore:

```text
S_O o tau_O o R_O o tau_O = S_O o tau_O on U
```

which is semantic sufficiency. ∎

## Converse failure: HE-EX-001 counterexample

The converse fails: semantic sufficiency does not imply microstate sufficiency.

Use `HE-EX-001`, where:

```text
X = Z_12
Y = {+, -}
F_+ = {11, 0, 1, 2, 3, 4}
F_- = {5, 6, 7, 8, 9, 10}
```

Let semantic space be:

```text
M = {+, -}
```

and let semantic lift be identity:

```text
S(+) = +
S(-) = -
```

Define reconstruction:

```text
R(+) = 0
R(-) = 5
```

Then for every `x in X`, `R(tau(x))` lies in the same trace fiber as `x`, so:

```text
tau(R(tau(x))) = tau(x)
```

Therefore:

```text
S(tau(R(tau(x)))) = S(tau(x))
```

so the interface is semantically sufficient on all of `X`.

But microstate sufficiency fails. For example:

```text
x = 1
R(tau(1)) = R(+) = 0 != 1
```

Thus semantic sufficiency does not imply microstate sufficiency.

## Rate-distortion framing

Let `X` be a random variable on latent states and let:

```text
Y = tau_O(X)
```

be the trace random variable. Since `Y` is a deterministic function of `X`:

```text
I(X;Y) = H(Y)
```

when entropies are finite.

Microstate sufficiency requires enough rate to recover `X`, i.e. zero distortion in `d_X`.

Semantic sufficiency requires zero semantic distortion:

```text
E[delta_sem^O(X)] = 0
```

which may occur at a lower rate than full microstate recovery.

Task sufficiency requires zero task distortion for a specified task and may occur at still lower rate.

## Semantic holography

Semantic holography is the regime where:

```text
E[delta_sem^O(X)] = 0 or approximately 0
```

while:

```text
E[epsilon_rec^O(X)] > 0
```

or equivalently the trace rate is below full microstate rate:

```text
H(Y) < H(X)
```

for finite uniform examples.

This is not physical AdS/CFT holography. It is an observer-relative information phenomenon: the trace preserves semantics while losing microstate detail.

## Worked rate-distortion computation on HE-EX-001

For the uniform distribution on `X = Z_12`:

```text
H(X) = log2(12) ≈ 3.585 bits
```

The two-state trace `Y = {+, -}` is balanced, so:

```text
H(Y) = 1 bit
```

The conditional entropy is:

```text
H(X | Y) = log2(6) ≈ 2.585 bits
```

The reconstruction above preserves semantics exactly:

```text
E[delta_sem(X)] = 0
```

but it does not recover microstate:

```text
H(X | Y) = log2(6) > 0
```

This gives a concrete semantic holographic gap: the interface carries 1 bit of semantic trace while losing `log2(6)` bits of microstate information.

## Relationship to Temporal Mechanics v0.24.1

Temporal Mechanics v0.24.1 §11 frames image / preimage discipline at substrate level. HE-PROJ-002 is the Heller-Einstein repository-level formalization of the sufficiency hierarchy for that discipline.

Bibliographic citation:

```text
Heller, Michael D. Temporal Mechanics and Emergence, v0.24.1 reconstructed editable source, 2026-05-08, §§11-12.
```

This remains a bibliographic manuscript citation, not a repo-pinned upstream.

## Boundaries

This document does not:

- derive quantum mechanics;
- derive the Born rule;
- claim semantic sufficiency implies microstate sufficiency;
- formalize a full task-sufficiency lattice;
- claim semantic holography is physical AdS/CFT holography;
- assert observer-independent semantics;
- collapse ontology to boundary traces.

## Reserved follow-up

`HE-PROJ-TASK-001` is reserved for the task-sufficiency lattice, including formal meet / join operations and task-family infimum results. That work requires explicit action maps, task losses, and admissibility hypotheses.

## Citation form

```text
[HE-PROJ-002 @ <merge-sha>]
[HE-INT-001 @ <merge-sha>]
[HE-EX-001 @ <merge-sha>]
[A-HE-PROJ-002 @ <merge-sha>]
```
