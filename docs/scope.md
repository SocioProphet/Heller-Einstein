# Heller-Einstein Scope

This document gives the conservative scope of the Einstein-Heller Interface Program. Full formal specifications land in later `HE-INT-*`, `HE-PROJ-*`, `HE-PHYS-*`, `HE-PLC-*`, and `HE-EX-*` content PRs.

## Pillar 1 — Typed Interface Ontology

Let `X` denote the latent or bulk state space. Bulk dynamics are represented by:

```text
Phi_t : X -> X
x_t = Phi_t(x_0)
```

For observer `O`, define a trace space `Y_O` and trace map:

```text
tau_O : X -> Y_O
```

Define an observer-relative semantic lift:

```text
S_O : Y_O -> M_O
```

The typed access chain is:

```text
x_t in X -> tau_O(x_t) in Y_O -> S_O(tau_O(x_t)) in M_O
```

Meaning is not inserted as a primitive bulk field. Meaning is an observer-relative lift from interface traces.

When available, a reconstruction map is:

```text
R_O : Y_O -> X
```

For `y in Y_O`, the compatible latent fiber is:

```text
F_y := tau_O^{-1}(y)
```

Observer-relative semantic equivalence is:

```text
x ~_O x' iff S_O(tau_O(x)) = S_O(tau_O(x'))
```

## Pillar 2 — Projection-Induced Stochasticity

The formal theorem will be specified in `HE-PROJ-001`.

Let `f : X -> X` be deterministic and let `tau : X -> Y` be surjective. For each `y in Y`, define `F_y := tau^{-1}(y)`. Let `mu_y` be a probability measure supported on `F_y`. Define:

```text
K(y, y') := mu_y({x in F_y : tau(f(x)) = y'})
```

Then `K` is a Markov kernel on `Y`. It is deterministic iff `tau o f` is `mu_y`-almost surely constant on each fiber `F_y`; otherwise the observer-level induced law is stochastic.

Interpretation: apparent probability can arise from projection loss without asserting that quantum theory has been derived. Per `A-HE-PROJ-001`, this does not derive quantum mechanics, the Born rule, noncommuting observables, or entanglement structure.

### Canonical exemplars

`HE-EX-001` will formalize the discrete phase cycle:

```text
X = Z_12
f(x) = x + 2 mod 12
Y = {+, -}
F_+ = {11,0,1,2,3,4}
F_- = {5,6,7,8,9,10}
```

With uniform fiber measures, the induced kernel is:

```text
K = [[2/3, 1/3], [1/3, 2/3]]
```

`HE-EX-002` will formalize the continuous phase flow on `S^1` with sampling interval `omega Delta t = pi/3`, producing the same kernel.

## Pillar 3 — Conservative Einstein-Cartan-Dirac Physical Core

The conservative physical core will be specified under `HE-PHYS-*`.

Microscopic action surface:

```text
S_EH^micro = S_grav + S_Dirac + S_phi + S_chi + S_int + S_grav,bdy + S_Sigma_O
```

Gravitational sector:

```text
S_grav = (1 / 2kappa) integral_M d^4x e (R_tilde - 2 Lambda)
```

Minimally coupled Dirac sector:

```text
S_Dirac = integral_M d^4x e [ i/2 (bar(psi) gamma^mu nabla_tilde_mu psi - (nabla_tilde_mu bar(psi)) gamma^mu psi) - m bar(psi) psi ]
```

Scalar projection field and pseudoscalar coherence field:

```text
S_phi = - integral_M d^4x e [ Z_phi/2 nabla_mu phi nabla^mu phi + V_phi(phi) ]
S_chi = - integral_M d^4x e [ Z_chi/2 nabla_mu chi nabla^mu chi + V_chi(chi) ]
```

Minimal interaction sector:

```text
S_int = integral_M d^4x e [ -lambda_phi phi bar(psi) psi + lambda_chi (nabla_mu chi) J_5^mu - W(phi, chi) ]
```

Observer-interface term on `Sigma_O`:

```text
S_Sigma_O = integral_{Sigma_O} d^3 xi sqrt(|h|) [ eta_phi/2 (tau_phi - hat(phi)_O)^2 + eta_chi/2 (tau_chi - hat(chi)_O)^2 + J_O^phi tau_phi + J_O^chi tau_chi ]
```

Effective torsion-eliminated branch: in minimal Einstein-Cartan theory with Dirac matter, algebraic torsion integrates out and produces a four-fermion contact term proportional to `J_5^mu J_{5 mu}`. The full expression and convention checks land in `HE-PHYS-002`.

## Sufficiency hierarchy preview

The full sufficiency hierarchy lands in `HE-PROJ-002`.

- Microstate sufficiency: reconstruction recovers the latent state on a declared subset.
- Semantic sufficiency: reconstruction preserves semantic lift.
- Task sufficiency: reconstruction is adequate for a declared task/loss.
- Semantic holography: semantic or task distortion is small while microstate reconstruction remains incomplete.

Microstate sufficiency implies semantic sufficiency; the converse fails. Task sufficiency is task-relative.

## Placeholder spaces

The placeholder chain:

```text
X_15 -> X_7 -> X_3 -> X_2
```

is typed, not topological. No claim is made that these are literal spheres, homogeneous spaces, or bundle bases. Per `A-HE-PLC-001`, topology and geometry require later content-specific instantiation.
