# HE-PROJ-ACT-INV-001 — Mode-Composition Law v0.1

Identifier: `HE-PROJ-ACT-INV-001`  
Status: active conditional capsule; frontier remains open  
Claim grade: modeling-choice-grade for the v0.1 routing law; theorem-grade for the v0.1 thresholded reachability characterization conditional on this law  
Proof form: v0.1.1 canonical proof refinement — quotient-map notation and contraction-primary admissibility  
Intended use: finite cyclic Fourier routing model for periodic activation spectral-attainability analysis  
Parents: `HE-PROJ-ACT-001`, `HE-PROJ-ACT-002`, `HE-PROJ-003`  
Anti-seed: `A-HE-PROJ-ACT-002`, `A-HE-PROJ-ACT-INV-001`

## 0. Modeling-choice warning

This document defines one admissible formalization of harmonic transfer under finite truncation. It is a definitional choice, not a theorem derived from `HE-PROJ-ACT-001` or `HE-PROJ-ACT-002`.

Alternative truncation, aliasing, folding, or parent-pattern conventions yield alternative routing laws. Any threshold theorem or effective-bandwidth theorem proved downstream is conditional on the routing law fixed here.

This warning is load-bearing. The routing law below must not be cited later as “the” canonical harmonic-transfer law unless a separate uniqueness or invariance theorem proves that competing conventions are equivalent for the downstream claim.

Downstream citations must use a conditional form, for example:

```text
conditional on HE-PROJ-ACT-INV-001 mode-composition law v0.1
```

## 1. Design decision for v0.1

This v0.1 spec uses a finite circular Fourier model with modular aliasing.

Reason: `HE-PROJ-ACT-INV-001` is meant to study what periodic activations can stably generate under finite representation. A hard cutoff would make high-frequency reach fail partly by fiat, because out-of-band harmonics would be erased by the truncation convention rather than by activation decay or contraction admissibility. Modular aliasing keeps out-of-band harmonic generation visible inside the finite model by folding high modes back into the finite frequency group.

The choice is still a modeling choice. It is selected for v0.1 because it is faithful to finite cyclic Fourier analysis and makes harmonic generation observable rather than silently discarded.

## 2. Sensitive convention: aliasing versus cutoff versus remainder

The load-bearing choice is the out-of-band rule. Three honest conventions are available:

1. Hard cutoff. Generated modes outside the finite band are dropped. This yields sparse routing and clean proofs, but imposes a bandwidth limit by the truncation rule itself.
2. Aliasing / folding. Generated modes outside the finite band wrap back into the finite frequency group. This yields a finite cyclic Fourier model. High harmonics remain visible, but the folding rule is itself a convention.
3. Truncation with remainder. Generated modes outside the finite band are tracked as an error/remainder mass. This is analytically honest but no longer gives a purely finite routing graph.

This v0.1 spec chooses modular aliasing. Later variants may define a cutoff model (`v0.1-cutoff`) or a remainder model (`v0.1-rem`) and compare threshold behavior across conventions.

## 3. Finite frequency group

Fix a positive integer `M >= 2`. Define the finite cyclic frequency group:

```text
G_M := Z / MZ
```

Let:

```text
K_M := {0, 1, ..., M-1}
```

be the representative mode set. Let:

```text
V_M := C^{G_M}
```

be the finite coefficient space with basis vectors `e_m` indexed by `m in G_M`.

For an integer `r in Z`, write:

```text
[r]_M
```

for its residue class in `G_M`. This is the v0.1 aliasing map. In code-oriented contexts this is the same operation previously written `alias_M(r)`.

## 4. Activation dictionary and Fourier coefficients

For each layer `i = 1,...,d`, choose a periodic activation profile:

```text
phi_i(t) = sum_{n in Z} phihat_i(n) exp(i n t)
```

For finite computation, choose a harmonic truncation radius `H_i` and define:

```text
N_i := { n in Z : |n| <= H_i and phihat_i(n) is retained }
```

The coefficient magnitude attached to harmonic index `n` is:

```text
a_i(n) := |phihat_i(n)|
```

The dictionary data for layer `i` are:

```text
D_i := (phi_i, N_i, phihat_i restricted to N_i)
```

This finite harmonic truncation is separate from the finite mode group `G_M`. The harmonic index `n` belongs to the activation expansion; the routed mode belongs to the finite representation group.

## 5. Layer parameters

Each layer has weight and bias data:

```text
w_i in Z
b_i in R / 2piZ
```

For v0.1, weights are restricted to integers so that frequency routing is a well-defined endomorphism of the finite cyclic frequency group:

```text
m -> [w_i m]_M
```

Noninteger weights are out of scope for v0.1. They require interpolation, non-lattice frequency models, or a continuous Fourier transform formulation.

Bias affects phase but not magnitude:

```text
|exp(i n b_i)| = 1
```

Therefore bias is recorded for phase-sensitive extensions but drops out of the magnitude-only attainability lemma.

The integer-weight restriction also changes the optimization class. Under v0.1, realization sets are lattice sets, not continuous regions. Under any bounded integer-weight search window, the downstream threshold problem is finite and discrete.

## 6. Parent patterns

For v0.1, the allowed parent pattern at layer `i` is a single incoming finite mode:

```text
q_i = m_{i-1} in G_M
```

This is intentionally minimal. It captures the routing effect of applying a scalar periodic activation to a single mode carrier.

A later multi-index version may allow:

```text
q_i = (m_{i-1,1}, ..., m_{i-1,k})
```

for products, sums, or intermodulation patterns. That is not part of v0.1.

## 7. v0.1 mode-composition law

Suppose the incoming carrier at layer `i` has finite mode:

```text
m_{i-1} in G_M
```

The activation harmonic `n_i in N_i` and integer weight `w_i` generate output mode:

```text
m_i = [n_i w_i m_{i-1}]_M
```

Thus the v0.1 routing relation is:

```text
m_{i-1} --(i,n_i,w_i)--> m_i
iff
m_i = [n_i w_i m_{i-1}]_M
```

The magnitude of this transfer is:

```text
T_i[m_i | m_{i-1}, n_i] := |phihat_i(n_i)|
```

when the routing equation holds, and:

```text
T_i[m_i | m_{i-1}, n_i] := 0
```

otherwise.

Equivalently, the transfer hyperkernel is:

```text
T_i[m_i | q_i]
```

where here:

```text
q_i = (m_{i-1}, n_i)
```

This is a single-carrier harmonic-routing law. It is not a full nonlinear coefficient-convolution law for arbitrary superpositions. It is the v0.1 finite routing model.

## 8. Transfer graph

For each layer `i`, define the directed labeled transfer graph:

```text
Graph_i(M,H_i,w_i)
```

with vertices `G_M` and directed edges:

```text
m_{i-1} -> m_i
```

labeled by harmonic `n_i` whenever:

```text
m_i = [n_i w_i m_{i-1}]_M
```

The edge weight is:

```text
edge_weight_i(m_{i-1}, n_i, m_i) = |phihat_i(n_i)|
```

A depth-`d` routing pattern is a path through the layer graphs:

```text
r = (m_0, n_1, m_1, n_2, ..., n_d, m_d)
```

such that every layer routing equation holds.

## 9. Target mask and target-ending paths

Let:

```text
P_target : G_M -> [0,1]
```

be a target mask.

A routing path `r` is target-ending if:

```text
P_target(m_d) > 0
```

The target-weighted routed amplitude is:

```text
A_T(r; Theta) := P_target(m_d) product_{i=1}^d |phihat_i(n_i)|
```

where:

```text
Theta = (M, d, D_i, H_i, w_i, b_i, L_phi_i, S, L_S, K, delta(K), P_target)
```

## 10. Layer transfer maxima and transfer ceiling

For each layer define:

```text
B_i^T := max_{n in N_i} |phihat_i(n)|
```

This equals the maximum edge weight in `Graph_i` if at least one edge realizes each retained harmonic.

Define the transfer ceiling:

```text
Ceiling_T(Theta) := product_{i=1}^d B_i^T
```

This is not the Heller-Einstein contraction ceiling. It is the transfer relaxation ceiling.

The independent contraction/stability ceiling inherited from `HE-PROJ-ACT-002` is:

```text
C_Lip(Theta) := L_S (product_i |w_i| L_phi_i) delta(K)
```

The two objects are distinct and must not be collapsed.

## 11. Contraction admissibility

Define:

```text
AdmNet(Theta) := [ C_Lip(Theta) < 1 ]
```

This is a condition on the full network parameterization, not on an individual routing path.

If `AdmNet(Theta)` fails, the contraction-attainability protocol is invalid for theorem-facing use. The transfer graph may still exist, but it is outside the stable regime reserved by `HE-PROJ-ACT-002`.

## 12. Valid routed-path set

Define:

```text
R(target, Theta)
```

to be the finite set of all target-ending routing paths:

```text
r = (m_0, n_1, m_1, ..., n_d, m_d)
```

satisfying all layer routing equations and `P_target(m_d)>0`.

Define the contraction-admissible routed-path set by:

```text
R_adm(target,Theta) := R(target,Theta) if AdmNet(Theta) holds,
                       invalid protocol otherwise
```

## 13. Normalized routed-transfer coefficient

For `Theta` satisfying `AdmNet(Theta)` and `Ceiling_T(Theta)>0`, define:

```text
Gamma_HE(r; target, Theta) := A_T(r; Theta) / Ceiling_T(Theta)
```

Equivalently:

```text
Gamma_HE(r; target, Theta)
  = P_target(m_d) product_i |phihat_i(n_i)| / product_i B_i^T
```

This is computed from the routing law and Fourier coefficients. It is not defined as `Attain/Ceiling`.

## 14. Fixed-network transfer-normalization lemma under this law

For fixed contraction-admissible `Theta`, define:

```text
Attain_T(target;Theta) := max_{r in R(target,Theta)} A_T(r;Theta)
```

If `R(target,Theta)` is nonempty and `Ceiling_T(Theta)>0`, then:

```text
Attain_T(target;Theta)
  = Ceiling_T(Theta) max_{r in R(target,Theta)} Gamma_HE(r;target,Theta)
```

This is a finite transfer-normalization lemma. It is not the full `HE-PROJ-ACT-INV-001` threshold theorem.

## 15. Ceiling-attainment criterion

The transfer ceiling is attained for the fixed network iff there exists a target-ending path:

```text
r* = (m_0*, n_1*, m_1*, ..., n_d*, m_d*)
```

such that:

```text
P_target(m_d*) = 1
```

and:

```text
|phihat_i(n_i*)| = B_i^T
```

for every layer `i`.

If no such routed path exists, then:

```text
Attain_T(target;Theta) < Ceiling_T(Theta)
```

## 16. Realizability sets

For a symbolic routing pattern:

```text
r = (m_0, n_1, m_1, ..., n_d, m_d)
```

define its realization set:

```text
Real(r)
```

as the set of network parameterizations `Theta` satisfying all routing equations:

```text
m_i = [n_i w_i m_{i-1}]_M for i=1,...,d
```

and all declared dictionary/truncation conditions:

```text
n_i in N_i,
P_target(m_d)>0
```

Define contraction-realizability by:

```text
Real_adm(r) := Real(r) intersection {Theta : C_Lip(Theta)<1}
```

A routing pattern is contraction-realizable iff:

```text
Real_adm(r) is nonempty
```

Because v0.1 restricts weights `w_i` to integers, `Real(r)` is not a continuous region in weight space. It is a finite or countable lattice subset, and under any declared bounded weight search window it is finite. Consequently, the v0.1 threshold problem is a discrete search over integer-weight networks and routed paths, not a continuous optimization. Continuous-feasibility language belongs only to later noninteger-weight variants.

## 17. Partial comparison characterization

Given the routing law above, define:

```text
Coeff(r) := P_target(m_d) product_i |phihat_i(n_i)|
```

Then the comparison objective reduces to:

```text
A_star(target,M,d)
  = max { Coeff(r) : r is target-routing and Real_adm(r) is nonempty }
```

This is a finite routing-realizability problem plus a Fourier-coefficient decay objective.

It is not a smooth Lagrangian problem in v0.1. Because weights are restricted to integers, both the routed harmonic indices and the contraction-realizable parameter choices are discrete once a bounded search window is declared. The comparison problem is therefore a finite combinatorial search in bounded v0.1 instances, not a continuous Lagrangian optimization.

## 18. Effective bandwidth set

For threshold `epsilon > 0`, define:

```text
B_eff(epsilon; M,d)
  := { m in G_M : exists routing r ending at m
       with Real_adm(r) nonempty and Coeff(r) >= epsilon }
```

Any downstream threshold theorem must be stated conditionally on this routing law.

## 19. Fixture A — pure sine, ceiling attainable

Let:

```text
M = 8,
d = 1,
phi(t) = sin(t),
N_1 = {1,-1},
|phihat(1)| = |phihat(-1)| = 1/2,
w_1 = 1,
P_target(1)=1
```

Choose input mode:

```text
m_0 = 1
```

and harmonic:

```text
n_1 = 1
```

Then:

```text
m_1 = [1 * 1 * 1]_8 = 1
```

The transfer amplitude is:

```text
A_T = 1/2
```

The transfer ceiling is:

```text
Ceiling_T = B_1^T = 1/2
```

Thus:

```text
Gamma_HE = 1,
Attain_T = Ceiling_T
```

This is the positive equality fixture.

## 20. Fixture B — nonlinear harmonic spread with strict defect

Let:

```text
M = 8,
d = 1,
phi(t) = sin(t) + alpha sin(3t),
0 < |alpha| < 1,
N_1 = {1,-1,3,-3},
w_1 = 1
```

Then:

```text
|phihat(1)| = |phihat(-1)| = 1/2,
|phihat(3)| = |phihat(-3)| = |alpha|/2
```

So:

```text
B_1^T = 1/2
```

If the target is mode `3` and input mode is `1`, the route uses harmonic `n=3`:

```text
m_1 = [3 * 1 * 1]_8 = 3
```

The target amplitude is:

```text
A_T = |alpha|/2
```

Thus:

```text
Gamma_HE = |alpha| < 1,
Attain_T < Ceiling_T
```

This is the strict-defect fixture: the target mode is reachable, but only through a lower-amplitude harmonic, so the transfer ceiling is not attained.

## 21. Fixture C — aliasing genuinely separates from cutoff

This fixture demonstrates the load-bearing convention difference between hard cutoff and modular aliasing.

Let:

```text
M = 8,
d = 1,
phi(t) = sin(5t),
N_1 = {5,-5},
w_1 = 1,
m_0 = 3,
n_1 = 5
```

The raw generated integer frequency is:

```text
r = n_1 w_1 m_0 = 5 * 1 * 3 = 15
```

Under a hard cutoff convention with finite band `K_8 = {0,1,...,7}`, the raw generated mode `15` is out of band. The route is dropped, so the corresponding target mode is unreachable through this transition.

Under the v0.1 modular aliasing convention:

```text
m_1 = [15]_8 = 7
```

Thus the same generated harmonic is retained as finite mode `7`, with amplitude:

```text
|phihat(5)|
```

So the two conventions give different reachability verdicts for the same network:

```text
hard cutoff: route dropped
modular aliasing: route reaches mode 7
```

This is the behavior v0.1 intentionally preserves and a hard-cutoff model suppresses. It is the concrete fixture justifying the aliasing choice in Sections 1 and 2.

## 22. Non-claims

This spec does not claim:

- this aliasing convention is canonical;
- hard cutoff is wrong;
- remainder tracking is unnecessary;
- the threshold theorem is convention-invariant;
- prime-sequence representation follows;
- the prime-modulus corollary says anything about prime numbers, prime gaps, Jacobsthal phenomena, or the Heller-Winters prime program; it concerns the ring/group structure of `Z/pZ` when the truncation modulus `M=p` is prime;
- representational bandwidth equals a product of layer frequencies;
- principal angles are the correct `Gamma` for this activation lineage;
- the May 12 spectral-learning geometry has been bridged into this frontier.

## 23. Downstream theorem boundary

Any downstream theorem must cite this spec in the form:

```text
conditional on HE-PROJ-ACT-INV-001 mode-composition law v0.1
```

and must state whether its conclusion is invariant under alternative conventions:

```text
hard cutoff,
modular aliasing,
reflection aliasing,
remainder tracking
```

If no invariance proof is supplied, the theorem is convention-conditional.

## 24. Threshold characterization theorem for v0.1

This section gives the canonical v0.1.1 proof form for the structural characterization supported by the v0.1 routing law. It is conditional on the modeling choices above.

### 24.1 Source support

The target-mode question is not meaningful unless the allowed source modes are declared. Therefore define a source support:

```text
S_0 subset G_M
```

If no source support is specified, the default convention is:

```text
S_0 = G_M
```

That default can make reachability less informative because the source mode may already lie in a favorable residue class. Downstream threshold claims should state the source support explicitly.

### 24.2 Threshold-clearing harmonic products

For threshold `epsilon > 0`, define:

```text
H_epsilon
  := { (n_1,...,n_d) in N_1 x ... x N_d : product_i a_i(n_i) >= epsilon }
```

Define the harmonic product residue set:

```text
HProd_epsilon
  := { [product_i n_i]_M : (n_1,...,n_d) in H_epsilon } subset G_M
```

This is the set of harmonic product residues whose coefficient product clears threshold.

### 24.3 Contraction-admissible weight products

Define the contraction factor directly:

```text
C_Lip(w_1,...,w_d)
  := L_S (product_i |w_i| L_phi_i) delta(K)
```

Define the nonzero contraction-admissible weight tuples by:

```text
W_adm^nz
  := { (w_1,...,w_d) in Z^d : w_i != 0 for all i, C_Lip(w_1,...,w_d) < 1 }
```

If:

```text
L_S delta(K) product_i L_phi_i > 0
```

then this is equivalently:

```text
product_i |w_i| < kappa,
kappa := 1 / (L_S delta(K) product_i L_phi_i)
```

The direct definition by `C_Lip < 1` is primary because it also handles edge cases where the reciprocal formula for `kappa` is not meaningful.

Define:

```text
WProd_adm^nz
  := { [product_i w_i]_M : (w_1,...,w_d) in W_adm^nz } subset G_M
```

### 24.4 Modular product sets

For subsets `A,B subset G_M`, define:

```text
A · B := { [ab]_M : a in A, b in B }
```

### 24.5 Effective bandwidth set

Define:

```text
B_eff^nz(epsilon; M,d,S_0)
```

to be the set of terminal modes `m in G_M` for which there exist:

```text
m_0 in S_0,
(n_1,...,n_d) in N_1 x ... x N_d,
(w_1,...,w_d) in W_adm^nz
```

such that the v0.1 recurrence:

```text
m_i = [n_i w_i m_{i-1}]_M
```

produces terminal mode `m_d = m`, and:

```text
product_i a_i(n_i) >= epsilon.
```

### 24.6 Theorem — v0.1 thresholded reachability characterization

Under the v0.1 mode-composition law:

```text
B_eff^nz(epsilon; M,d,S_0)
  = S_0 · HProd_epsilon · WProd_adm^nz.
```

Equivalently, `m in G_M` is threshold-reachable iff there exist:

```text
m_0 in S_0,
(n_1,...,n_d) in H_epsilon,
(w_1,...,w_d) in W_adm^nz
```

such that:

```text
m = [m_0 product_i n_i product_i w_i]_M.
```

### 24.7 Proof

First prove the path-collapse identity. For any routed path satisfying:

```text
m_i = [n_i w_i m_{i-1}]_M,
```

we claim:

```text
m_d = [m_0 product_i n_i product_i w_i]_M.
```

For `d=1`, this is exactly the routing law:

```text
m_1 = [n_1 w_1 m_0]_M.
```

Assume the identity holds through depth `j`:

```text
m_j = [m_0 product_{i=1}^j n_i product_{i=1}^j w_i]_M.
```

Then by the routing law:

```text
m_{j+1} = [n_{j+1} w_{j+1} m_j]_M.
```

The quotient map `Z -> Z/MZ` commutes with multiplication, so substituting the induction hypothesis gives:

```text
m_{j+1}
  = [m_0 product_{i=1}^{j+1} n_i product_{i=1}^{j+1} w_i]_M.
```

Thus the path-collapse identity holds by induction.

Now prove the forward inclusion. Let:

```text
m in B_eff^nz(epsilon; M,d,S_0).
```

Then there exists a routed path with source `m_0 in S_0`, harmonic tuple `(n_i)`, nonzero contraction-admissible weight tuple `(w_i)`, and terminal mode `m_d=m`, such that:

```text
product_i a_i(n_i) >= epsilon.
```

Therefore `(n_1,...,n_d) in H_epsilon`, so:

```text
[product_i n_i]_M in HProd_epsilon.
```

Also `(w_1,...,w_d) in W_adm^nz`, so:

```text
[product_i w_i]_M in WProd_adm^nz.
```

By the path-collapse identity:

```text
m = [m_0 product_i n_i product_i w_i]_M.
```

Hence:

```text
m in S_0 · HProd_epsilon · WProd_adm^nz.
```

Now prove the reverse inclusion. Let:

```text
m in S_0 · HProd_epsilon · WProd_adm^nz.
```

Then there exist `m_0 in S_0`, a harmonic product residue from some tuple `(n_1,...,n_d) in H_epsilon`, and a weight product residue from some tuple `(w_1,...,w_d) in W_adm^nz`, such that:

```text
m = [m_0 product_i n_i product_i w_i]_M.
```

The key independence property is specific to v0.1. The harmonic choices `n_i` and weight choices `w_i` are independently selectable at each layer. The retained harmonic set `N_i` is fixed by the activation dictionary. The contraction condition constrains only the product of the weight magnitudes. No v0.1 rule couples the admissibility of `n_i` to the chosen `w_i`, beyond the routing equation determining the next mode. Since both tuples have the same fixed depth `d`, the harmonic tuple and weight tuple co-deploy layer-by-layer.

Define a routed path recursively by:

```text
m_i = [n_i w_i m_{i-1}]_M.
```

This path is valid by construction. Its harmonic tuple lies in `H_epsilon`, so its coefficient product is at least `epsilon`. Its weight tuple lies in `W_adm^nz`, so it is contraction-admissible and nondegenerate. By the path-collapse identity, its terminal mode is exactly `m`. Therefore:

```text
m in B_eff^nz(epsilon; M,d,S_0).
```

Both inclusions hold, so:

```text
B_eff^nz(epsilon; M,d,S_0)
  = S_0 · HProd_epsilon · WProd_adm^nz.
```

This proves the theorem.

This independence is specific to v0.1. It may fail in a multi-index intermodulation law where harmonic admissibility depends on the routed carrier or where parent-pattern constraints couple `n_i` and `w_i`.

### 24.8 What this theorem closes

This closes the v0.1 structural characterization of thresholded reachability. It is stronger than a bounded enumeration procedure: it gives an if-and-only-if product-set condition.

The comparison problem is no longer merely “run finite search” under v0.1. It is:

```text
compute the modular product set generated by source support,
threshold-clearing harmonic products,
and contraction-admissible weight products.
```

### 24.9 What remains open

This theorem is conditional on v0.1 modeling choices and does not prove convention-invariance. Open items remain:

```text
1. compare modular aliasing with hard cutoff and remainder tracking;
2. handle noninteger weights;
3. handle full multi-index intermodulation instead of single-carrier routing;
4. characterize WProd_adm^nz in closed form for arbitrary M and contraction data;
5. characterize product sets over composite M beyond enumeration;
6. add phase-sensitive cancellation if complex phases matter;
7. connect this activation-routing theorem to the May 12 eigenbasis / unitary / gate geometry, if desired.
```

### 24.10 Useful corollaries

#### Prime modulus corollary

If `M=p` is prime and zero modes are excluded, then all nonzero modes lie in the multiplicative group `F_p^*`. If `S_0`, `HProd_epsilon`, and `WProd_adm^nz` are subsets of `F_p^*`, then:

```text
B_eff^nz(epsilon;p,d,S_0)
  = S_0 HProd_epsilon WProd_adm^nz
```

inside the group `F_p^*`.

If the subgroup generated by `HProd_epsilon` and `WProd_adm^nz` is all of `F_p^*`, then each source mode reaches its full multiplicative coset; if `S_0` contains one nonzero element, the reachable set is that source element times the generated subgroup.

This corollary concerns the ring/group structure of `Z/pZ` when the truncation modulus `M=p` is prime. It is not a statement about prime numbers, prime gaps, Jacobsthal phenomena, or the Heller-Winters prime program.

#### Composite modulus warning

For composite `M`, nonzero residues are not all units. Multiplication can move modes into different gcd strata. A sharper characterization can be obtained prime-power factor by prime-power factor using the Chinese remainder theorem, but that refinement is not part of v0.1.

### 24.11 Fixture D — threshold product-set check

Let:

```text
M = 8,
d = 1,
S_0 = {1},
phi(t) = sin(t) + alpha sin(3t),
0 < |alpha| < 1,
N_1 = {1,3},
w_1 in {1},
C_Lip(w_1) < 1.
```

If:

```text
epsilon <= |alpha|/2
```

then:

```text
H_epsilon = {1,3},
HProd_epsilon = {1,3},
WProd_adm^nz = {1},
B_eff^nz = {1,3}.
```

If:

```text
|alpha|/2 < epsilon <= 1/2
```

then:

```text
H_epsilon = {1},
HProd_epsilon = {1},
WProd_adm^nz = {1},
B_eff^nz = {1}.
```

This fixture shows that the effective bandwidth threshold is governed by coefficient decay: the third harmonic is reachable as a route, but it disappears from `B_eff` when the threshold exceeds its Fourier coefficient magnitude.

## 25. Version boundary

`HE-PROJ-ACT-INV-001-mode-composition-law v0.1` is sufficient to support:

```text
fixed-network transfer-normalization lemma;
v0.1 thresholded reachability characterization;
finite fixtures for equality, strict defect, aliasing, and threshold loss.
```

It is not sufficient to support:

```text
noninteger-weight threshold theorem;
cutoff-invariant theorem;
remainder-invariant theorem;
full superposition/intermodulation theorem;
prime-sequence depth lower bound;
May 12 spectral-learning bridge theorem.
```

## Citation form

```text
[HE-PROJ-ACT-INV-001 mode-composition law v0.1 @ <merge-sha>]
[A-HE-PROJ-ACT-INV-001 @ <merge-sha>]
```

Downstream theorem claims must preserve the v0.1 conditionality unless they supply an explicit convention-invariance proof.
