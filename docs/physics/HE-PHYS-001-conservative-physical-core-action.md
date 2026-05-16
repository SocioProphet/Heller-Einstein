# HE-PHYS-001 — Conservative Physical-Core Action

Identifier: `HE-PHYS-001`  
Parent interface ontology: `HE-INT-001 @ 59d41f8d7691937322355f1ab57243884ad81a1c`  
Claim grade: transcription-grade / rendered-page verified  
Status: active after this PR  
Anti-seed: `A-HE-PHYS-001`, `A-HE-PHYS-002`, `A-HE-PHYS-003`, `A-HE-PHYS-004`

## Scope

This document records the conservative Einstein-Heller physical-core action from `einstein_heller_v1_7_verified_source_candidate.pdf`, Section 3.

It is **transcription-grade**, not derivation-grade. The source candidate itself marks the physical-action sector as rendered-page verified and convention-pending. This file therefore records the action sectors and the minimal Einstein-Cartan torsion-elimination result, but it does not certify all variational conventions.

The equations of motion are reserved for `HE-PHYS-002`. They are not canonicalized here.

## Source and claim grade

Source:

```text
einstein_heller_v1_7_verified_source_candidate.pdf, 2026-05-08, Section 3 and Appendix B.
```

Provenance record:

```text
docs/provenance/einstein-heller-v1_7.md
```

Claim grade:

```text
transcription-grade / rendered-page verified
```

This means:

- the sectors and integrands are recorded as the conservative v1.7 source candidate presents them;
- the action is citable as a Heller-Einstein repository object after merge;
- native-source convention verification remains pending;
- derived equations of motion are deferred to `HE-PHYS-002`.

## Total microscopic action

The microscopic conservative physical-core action is:

```text
S_EH^micro = S_grav + S_Dirac + S_phi + S_chi + S_int + S_grav,bdy + S_Sigma_O
```

where the sectors are given below.

## Gravitational sector

```text
S_grav = (1 / 2kappa) integral_M d^4x e (R_tilde - 2 Lambda)
```

where:

- `e = sqrt(-g)` is the tetrad determinant / volume density;
- `kappa = 8 pi G`;
- `R_tilde` is the scalar curvature of the metric-compatible torsionful connection;
- `Lambda` is the cosmological constant.

Boundary completion is typed but convention-dependent; see `S_grav,bdy` below and `A-HE-PHYS-003`.

## Dirac sector

The minimally coupled Dirac sector is:

```text
S_Dirac = integral_M d^4x e [
  (i/2)(bar(psi) gamma^mu nabla_tilde_mu psi - (nabla_tilde_mu bar(psi)) gamma^mu psi)
  - m bar(psi) psi
]
```

where `nabla_tilde` is the spin connection with torsion.

## Scalar projection field

The scalar projection field `phi` has action:

```text
S_phi = - integral_M d^4x e [
  (Z_phi / 2) nabla_mu phi nabla^mu phi + V_phi(phi)
]
```

`phi` is the conservative projection field. The potential `V_phi` is not determined in this PR.

## Pseudoscalar coherence field

The pseudoscalar coherence field `chi` has action:

```text
S_chi = - integral_M d^4x e [
  (Z_chi / 2) nabla_mu chi nabla^mu chi + V_chi(chi)
]
```

`chi` is the conservative pseudoscalar coherence field. The potential `V_chi` is not determined in this PR.

## Minimal interaction sector

The minimal interaction sector is:

```text
S_int = integral_M d^4x e [
  - lambda_phi phi bar(psi) psi
  + lambda_chi (nabla_mu chi) J_5^mu
  - W(phi, chi)
]
```

where the axial current is:

```text
J_5^mu = bar(psi) gamma^mu gamma^5 psi
```

The interaction potential `W(phi, chi)` is not determined in this PR.

## Gravitational boundary sector

The gravitational boundary sector is written:

```text
S_grav,bdy
```

and remains typed but unspecified at this level. The correct completion depends on the chosen boundary data and first-order / metric formulation.

Per `A-HE-PHYS-003`, this PR does not assert that a specific Gibbons-Hawking-York, Holst-tetrad, or other boundary completion is canonical without declaring boundary data.

## Observer-interface sector

Let `Sigma_O` be an observer hypersurface with induced metric determinant `h`. The observer-interface term is:

```text
S_Sigma_O = integral_{Sigma_O} d^3 xi sqrt(|h|) [
  (eta_phi / 2)(tau_phi - phi_hat_O)^2
  + (eta_chi / 2)(tau_chi - chi_hat_O)^2
  + J_O^phi tau_phi
  + J_O^chi tau_chi
]
```

This is the physical-core interface term. It couples boundary trace variables to observer-side target data and sources.

## Interface interpretation

`S_Sigma_O` is the dynamical realization of the `HE-INT-001` trace-map vocabulary in the conservative physical core.

The interface ontology supplies:

```text
X --tau_O--> Y_O --S_O--> M_O
```

The physical core realizes a boundary trace surface through:

```text
tau_phi, tau_chi on Sigma_O
```

with observer data:

```text
phi_hat_O, chi_hat_O, J_O^phi, J_O^chi
```

The term does not collapse bulk ontology to the boundary. The bulk fields and the boundary traces remain typed separately. Per `A-HE-INT-001`, ontology does not collapse to boundary traces.

## Boundary-condition structure

Varying the interface term produces Robin-type boundary-condition contributions for the scalar and pseudoscalar trace variables. The schematic form is:

```text
normal derivative term + eta_phi (tau_phi - phi_hat_O) + J_O^phi = 0
normal derivative term + eta_chi (tau_chi - chi_hat_O) + J_O^chi = 0
```

This PR records only the structural Robin form. The full sign conventions, outward-normal orientation, and matching to the bulk scalar/pseudoscalar variations are reserved for `HE-PHYS-002`.

## Torsion elimination: minimal Einstein-Cartan branch

In the minimal Einstein-Cartan branch with Dirac matter, torsion is algebraic. Eliminating torsion yields the standard axial-current four-fermion contact term:

```text
(3 kappa / 16) J_5^mu J_{5 mu}
```

in the effective action, with convention-dependent sign controlled by metric and gamma-matrix choices.

This is the standard Hehl-Datta / Einstein-Cartan-Dirac result. It is recorded here as the independently checkable part of the physical core.

Per `A-HE-PHYS-002`, this result belongs to the minimal algebraic-torsion branch. Propagating-torsion alternatives are outside this conservative surface.

## Effective-action pointer

The effective torsion-eliminated action has the same scalar, pseudoscalar, interaction, gravitational-boundary, and observer-interface sectors, plus the axial-current contact term above. The full convention-checked effective action and its equations are reserved for `HE-PHYS-002`.

## Reserved EoM document

`HE-PHYS-002` is reserved for:

- Einstein equation and stress-tensor decomposition;
- effective Dirac equation with axial-current contact term;
- scalar and pseudoscalar equations;
- full interface boundary conditions on `Sigma_O`;
- convention and outward-normal verification.

This split is deliberate: `HE-PHYS-001` records the action; `HE-PHYS-002` records variations and convention-dependent derived objects.

## Non-claims

This document does not:

- derive the Standard Model gauge group;
- derive charge assignments;
- derive anomaly cancellation;
- derive fermion-family structure;
- determine `V_phi`, `V_chi`, or `W(phi, chi)`;
- certify all sign, index, orientation, or outward-normal conventions;
- assert a specific gravitational boundary completion;
- derive quantum mechanics or the Born rule;
- assert that interface boundary data collapses the bulk;
- import speculative emergent-charge or higher-sphere ontology content.

## Citation form

```text
[HE-PHYS-001 @ <merge-sha>]
[HE-INT-001 @ 59d41f8d7691937322355f1ab57243884ad81a1c]
[A-HE-PHYS-001 @ <merge-sha>]
[A-HE-PHYS-002 @ <merge-sha>]
[A-HE-PHYS-003 @ <merge-sha>]
[A-HE-PHYS-004 @ <merge-sha>]
```

## Versioning

This is `HE-PHYS-001 v1.0`. Any PR that changes the action sectors, adds or removes fields, or promotes the document from transcription-grade to derivation-grade requires major-version review.
