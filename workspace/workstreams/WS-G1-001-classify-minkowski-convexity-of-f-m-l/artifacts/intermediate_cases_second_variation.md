# Second-Variation Reduction For The Intermediate Cases

Date: 2026-05-30

## Purpose

The initial report used an unsupported global quotient-convexity statement. This
artifact replaces that vague black box by a precise local inequality whose proof
would imply the remaining intermediate cases `2 <= m <= n-1`.

This is a reduction, not a completed proof.

## Setup

Fix a full-dimensional convex body `L` and put

`B(K) = V(K[n-1],L)`.

Let `d = n-1`, `r = m-1`, so that `1 <= r <= d-1` in the intermediate cases.
Up to a positive normalization constant,

`A(K) = D_L^r B(K)`

is `V(K[n-m],L[m])`. Thus the desired functional has the same convexity as

`Phi(K) = A(K) / B(K)`.

Work locally at a full-dimensional body `K` along a support-function direction
`Y`. Formally, write directional derivatives as

`B_1 = D_Y B`, `B_2 = D_Y^2 B`, `A_1 = D_Y A`, `A_2 = D_Y^2 A`.

Then

`Phi'' >= 0`

is equivalent to

`A_2 B^2 - A B_2 B - 2 A_1 B_1 B + 2 A B_1^2 >= 0`.

## Primitive Decomposition

Decompose

`Y = aK + Z`

where `Z` is primitive with respect to `B` at `K`, i.e.

`D_Z B = 0`.

Since `B` is homogeneous of degree `d`,

`a = D_Y B / (d B)`.

Using homogeneity of `A`, whose degree is `d-r`, one obtains

`B_1 = d a B`,

`B_2 = d(d-1)a^2 B + D_Z^2 B`,

`A_1 = (d-r)a A + D_Z A`,

`A_2 = (d-r)(d-r-1)a^2 A + 2(d-r)a D_Z A + D_Z^2 A`.

Substitution and cancellation give the exact expression

`A_2 B^2 - A B_2 B - 2 A_1 B_1 B + 2 A B_1^2`

`= B * (B D_Z^2 A - A D_Z^2 B - 2r a B D_Z A + r(r+1)a^2 A B)`.

Thus the intermediate convexity problem is equivalent to nonnegativity of the
quadratic in `a`:

`B D_Z^2 A - A D_Z^2 B - 2r a B D_Z A + r(r+1)a^2 A B >= 0`

for every `B`-primitive direction `Z`.

## Exact Missing Inequality

Since the coefficient of `a^2` is positive for `r >= 1`, the preceding
quadratic is nonnegative for all `a` if and only if its minimum is nonnegative:

`B D_Z^2 A - A D_Z^2 B - (r/(r+1)) B (D_Z A)^2 / A >= 0`

for every `Z` satisfying `D_Z B = 0`.

Equivalently,

`D_Z^2 A / A - (r/(r+1))(D_Z A / A)^2 >= D_Z^2 B / B`.

This is the precise strengthened local Hodge-Riemann/Lorentzian inequality
needed for `2 <= m <= n-1`.

## Checks

- For `m = 1`, `r = 0` and the quotient is constant.
- For `m = n`, `r = d`; then `A` is constant, and the inequality reduces to
  `D_Z^2 B <= 0` on the primitive hyperplane, which is the usual
  Hodge-Riemann/Alexandrov-Fenchel sign condition.
- Fixed-seed searches on boxes, random polytopes, and zonotopes found no
  counterexample in intermediate cases, but these computations are not proof.

## Provenance

- Algebraic cancellation checked symbolically in the Codex workstream.
- Hodge-Riemann sign comparison uses the standard primitive form intuition from
  Alexandrov-Fenchel/Lorentzian polynomial theory.
- This reduction was created after independent reviewers rejected the earlier
  unsupported global quotient-convexity claim.

## Remaining Work

Find a source or prove the exact missing inequality above for mixed volumes of
convex bodies. Potential source families:

- local Alexandrov-Fenchel inequalities for mixed area measures;
- local Hodge index inequalities for Lorentzian polynomials;
- Hessian quotient concavity methods, if they can be transferred from pointwise
  Hessian operators to mixed-volume functionals without extra assumptions.
