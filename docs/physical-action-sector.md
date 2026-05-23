# Conservative Physical-Action Sector

Status: Heller-Einstein v0.1 physical-action surface.  
Source: Einstein-Heller Interface Program v1.7 verified source candidate.  
Primary identifiers: `HE-PHYS-*`.  
Claim level: rendered-page verified / method-grade pending native-source and convention checks.

## Purpose

This document records the conservative physical-action sector from the v1.7 source candidate in repository-native form.

The sector is structurally useful but conservative. It is not promoted to theorem-grade by this import.

## HE-PHYS-001 — Microscopic action decomposition

Grade: rendered-page verified / method-grade.

The microscopic Einstein-Heller action is decomposed as:

```text
S_EH^micro = S_grav + S_Dirac + S_phi + S_chi + S_int + S_grav,bdy + S_Sigma_O
```

The conservative core is Einstein-Cartan-Dirac plus:

- scalar projection field `phi`;
- pseudoscalar coherence field `chi`;
- observer-interface boundary term on `Sigma_O`.

## HE-PHYS-002 — Gravitational sector

Grade: rendered-page verified / method-grade.

The gravitational sector is:

```text
S_grav = (1 / 2 kappa) integral_M d^4x e (R_tilde - 2 Lambda)
```

where:

```text
e = sqrt(-g)
kappa = 8 pi G
R_tilde = scalar curvature of the metric-compatible torsionful connection
```

## HE-PHYS-003 — Dirac sector

Grade: rendered-page verified / method-grade.

The minimally coupled Dirac sector is:

```text
S_Dirac = integral_M d^4x e [
  (i/2)(bar(psi) gamma^mu nabla_tilde_mu psi - (nabla_tilde_mu bar(psi)) gamma^mu psi)
  - m bar(psi) psi
]
```

This is the conservative Einstein-Cartan-Dirac branch.

## HE-PHYS-004 — Scalar projection and pseudoscalar coherence sectors

Grade: rendered-page verified / method-grade.

Scalar projection field:

```text
S_phi = - integral_M d^4x e [
  (Z_phi / 2) nabla_mu phi nabla^mu phi + V_phi(phi)
]
```

Pseudoscalar coherence field:

```text
S_chi = - integral_M d^4x e [
  (Z_chi / 2) nabla_mu chi nabla^mu chi + V_chi(chi)
]
```

## HE-PHYS-005 — Minimal interaction sector

Grade: rendered-page verified / method-grade.

The minimal interaction sector is:

```text
S_int = integral_M d^4x e [
  - lambda_phi phi bar(psi) psi
  + lambda_chi (nabla_mu chi) J_5^mu
  - W(phi, chi)
]
```

The derivative pseudoscalar coupling to the axial current is structurally important for later realization questions, but v0.1 does not identify it with any Heller-Godel carry defect or Yang-Mills object.

## HE-PHYS-006 — Observer-interface boundary term

Grade: rendered-page verified / method-grade.

The observer-interface term is:

```text
S_Sigma_O = integral_Sigma_O d^3 xi sqrt(|h|) [
  (eta_phi / 2)(tau_phi - hat(phi)_O)^2
  + (eta_chi / 2)(tau_chi - hat(chi)_O)^2
  + J_phi^O tau_phi
  + J_chi^O tau_chi
]
```

The gravitational boundary term `S_grav,bdy` remains typed in the microscopic first-order branch because the correct completion depends on the chosen boundary data.

## HE-PHYS-007 — Torsion-eliminated effective action

Grade: rendered-page verified / method-grade.

In the minimal Einstein-Cartan branch, torsion is algebraic and can be integrated out. For Dirac matter, the effective torsion-free action includes the standard axial-current four-fermion term:

```text
(3 kappa / 16) J_5^mu J_{5 mu}
```

The effective action is schematically:

```text
S_EH^eff = integral_M d^4x e [
  (1 / 2 kappa)(R_circ - 2 Lambda)
  + bar(psi)(i gamma^mu nabla_circ_mu - m) psi
  + (3 kappa / 16) J_5^mu J_{5 mu}
  - (Z_phi / 2)(nabla phi)^2 - V_phi(phi)
  - (Z_chi / 2)(nabla chi)^2 - V_chi(chi)
  - lambda_phi phi bar(psi) psi
  + lambda_chi (nabla_mu chi) J_5^mu
  - W(phi, chi)
] + S_grav,bdy + S_Sigma_O
```

The source notes one long-line reconstruction from component terms. This repository preserves that rendered-page verification status.

## HE-PHYS-008 — Equations of motion

Grade: rendered-page verified / method-grade.

Metric variation gives:

```text
G_circ_{mu nu} + Lambda g_{mu nu}
 = kappa (T_psi + T_4f + T_phi + T_chi + T_int)_{mu nu}
```

Scalar projection field:

```text
Z_phi Box phi - V_phi'(phi) - partial_phi W(phi, chi) = lambda_phi bar(psi) psi
```

Coherence field:

```text
Z_chi Box chi - V_chi'(chi) - partial_chi W(phi, chi) = lambda_chi nabla_mu J_5^mu
```

Effective Dirac equation:

```text
(i gamma^mu nabla_circ_mu - m
 + (3 kappa / 8) J_5_mu gamma^mu gamma^5
 - lambda_phi phi
 + lambda_chi (nabla_mu chi) gamma^mu gamma^5) psi = 0
```

## HE-PHYS-009 — Interface boundary conditions

Grade: rendered-page verified / method-grade.

The scalar-field interface boundary conditions are:

```text
-Z_phi n^mu nabla_mu phi + eta_phi (tau_phi - hat(phi)_O) + J_phi^O = 0 on Sigma_O
```

and:

```text
-Z_chi n^mu nabla_mu chi
 + lambda_chi n_mu J_5^mu
 + eta_chi (tau_chi - hat(chi)_O)
 + J_chi^O = 0 on Sigma_O
```

The sign conventions are tied to the outward-normal convention stated in the source. Native-source convention verification remains a future obligation.

## Deferred material

The following are not imported as active v0.1 physical-action claims:

- emergent charge;
- Heller-Dirac-derived physical structure claims;
- higher-sphere ontology;
- Standard Model gauge group derivation;
- charge assignments;
- anomaly cancellation;
- fermion-family structure.

## Non-claims

This document does not derive quantum mechanics.

This document does not derive the Born rule.

This document does not derive the Standard Model gauge group.

This document does not derive charge assignments, anomaly cancellation, or fermion families.

This document does not certify all physical sign conventions beyond the rendered-page verification status.

This document does not promote the physical-action sector to theorem-grade.

This document does not transfer proof content into Heller-Godel, Heller-Dirac, Yang-Mills, or any Clay-program repository.
