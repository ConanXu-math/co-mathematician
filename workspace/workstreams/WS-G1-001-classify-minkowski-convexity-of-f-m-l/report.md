# Workstream Report

## Summary

The classification supported by the current proof artifacts is:

For `n >= 2` and `0 <= m <= n`, the assertion

`for every fixed full-dimensional convex body L, F_{m,L} is Minkowski convex in K`

holds if and only if

`m = 1`, or `m = n`, or `(n,m) = (3,2)`.

The case `m=0` fails in every dimension by an explicit box counterexample. The
endpoint cases `m=1` and `m=n` hold in every dimension. The exceptional
three-dimensional intermediate case `n=3,m=2` holds by a direct Lorentzian
bilinear-form argument. Every intermediate case in dimension `n>=4` fails by a
bivariate volume-polynomial counterexample realized by Shephard's theorem and
then lifted by products.

This report passed independent logic and citation review after the bivariate
counterexamples and positive-case provenance were added.

## Conventions

Let `K^n` denote full-dimensional compact convex bodies in `R^n`. Mixed-volume
notation follows the convention that `V(K[n-m],L[m])` has `n-m` arguments equal
to `K` and `m` arguments equal to `L`. Minkowski convexity means

`F((1-t)K_0 + tK_1) <= (1-t)F(K_0) + tF(K_1)`

for `0 <= t <= 1`.

## Theorem

For `n >= 2`, the functional

`F_{m,L}(K) = V(K[n-m],L[m]) / V(K[n-1],L)`

is Minkowski convex in `K` for every fixed full-dimensional convex body `L` if
and only if

`m = 1`, or `m = n`, or `(n,m) = (3,2)`.

## Positive Cases

### The Case `m = 1`

Here the numerator and denominator are the same mixed volume:

`F_{1,L}(K) = V(K[n-1],L) / V(K[n-1],L) = 1`.

Thus `F_{1,L}` is constant, hence Minkowski convex.

### The Case `m = n`

Here

`F_{n,L}(K) = V(L[n]) / V(K[n-1],L)`.

By the mixed-volume Brunn-Minkowski theorem, the function

`K -> V(K[n-1],L)^(1/(n-1))`

is Minkowski concave on full-dimensional convex bodies. Concretely, this is
obtained from Wang's Theorem 2.7 with `m=n-1`, fixed final body `L`, and
Wang's Lemma 2.5 converting log-concavity plus homogeneity into
Brunn-Minkowski concavity; see
`artifacts/wang_2018_remark_alexandrov_fenchel.txt:224-266`.

The reciprocal of a positive concave function is convex, and a positive convex
function raised to the power `n-1 >= 1` remains convex. Hence `F_{n,L}` is
Minkowski convex.

### The Exceptional Case `n = 3, m = 2`

In dimension three,

`F_{2,L}(K) = V(K,L,L) / V(K,K,L)`.

Set `q(X,Y)=V(X,Y,L)`. The Alexandrov-Fenchel/Hodge-Riemann theorem says that
this bilinear form is Lorentzian modulo translations, so on the primitive
hyperplane `{Z : q(K,Z)=0}` the form is non-positive.

For provenance: Branden-Leake Lemma 2.3 gives the equivalence between
Alexandrov-Fenchel, Lorentzian signature, and primitive negative
semidefiniteness for a symmetric bilinear form; Corollary 6.6 supplies
Alexandrov-Fenchel for convex bodies. See
`artifacts/branden_leake_2023_lorentzian_polynomials_on_cones.txt:230-285`
and `:1448-1472`.

Writing a direction as `Y=aK+Z` with `q(K,Z)=0`, direct differentiation of
`Phi=q(K,L)/q(K,K)` reduces convexity to

`q(K,K) q(Z,L)^2 <= -q(K,L)^2 q(Z,Z)`.

Projecting `L` to the primitive hyperplane and applying Cauchy-Schwarz for the
positive semidefinite form `-q` proves this inequality. The complete calculation
is saved in `artifacts/n3_m2_lorentzian_bilinear_proof.md`.

Thus the classification is fully positive in dimensions `n=2` and `n=3`, apart
from the separately disproved `m=0`.

## Negative Cases

### The Case `m = 0`

Let `L = Q = [0,1]^n`. For an axis-aligned box

`B(a) = [0,a_1] x ... x [0,a_n]`,

Minkowski addition corresponds to addition of side-length vectors. The volume
polynomial gives

`F_{0,Q}(B(a)) = n / sum_i (1/a_i)`.

Choose `R > 1`,

`a = (R,1,1,...,1)`,

`b = (1,R,1,...,1)`.

The midpoint has side lengths

`c = ((R+1)/2, (R+1)/2, 1, ..., 1)`.

Midpoint convexity would require

`4R >= (R+1)^2`,

which is false for every `R != 1`. Hence `m=0` fails in every dimension
`n>=2`.

### All Intermediate Cases In Dimension `n >= 4`

The artifact `artifacts/bivariate_volume_polynomial_counterexamples.md`
constructs counterexamples for every `n>=4` and `2<=m<=n-1`.

The key reduction is this. If

`f(x,y)=vol_n(xP+yQ)`,

and we fix `L=Q`, `K=xP+yQ`, then

`F_{m,Q}(K)`

is a positive constant multiple of

`R_m(x,y) = (partial_y^m f)/(partial_y f)`.

Thus a negative Hessian determinant for `R_m` at a positive point disproves
Minkowski convexity of `F_{m,Q}`.

Use the bivariate Lorentzian polynomial

`f_N(x,y)=3(x+y)^N - 2x^N - 2y^N`.

Its normalized coefficient sequence is `1,3,...,3,1`, which is log-concave.
By Shephard's construction, as recorded by Branden-Huh, this polynomial is the
volume polynomial of a pair of `N`-dimensional rational polytopes.

For `N=4,m=2`, the Hessian determinant of

`(partial_y^2 f_4)/(partial_y f_4)`

at `(2,1)` is `-3456/493039`.

For `N=4,m=3`, the Hessian determinant of

`(partial_y^3 f_4)/(partial_y f_4)`

at `(4,1)` is `-147744/19356878641`.

For `m>=4`, take the base dimension `N=m+1`. The determinant at `(x,y)=(2,1)`
is negative by the explicit formula in
`artifacts/bivariate_volume_polynomial_counterexamples.md`.

Finally, product lifting sends a base counterexample in dimension `N` to every
higher dimension `n>=N`: replace `P,Q` by

`P x [0,1]^r`, `Q x [0,epsilon]^r`,

where `r=n-N` and `epsilon>0` is sufficiently small. The volume polynomial is

`f(x,y)(x+epsilon y)^r`,

and the negative Hessian determinant persists by continuity as
`epsilon -> 0+`.

Therefore every intermediate case `n>=4`, `2<=m<=n-1`, fails.

## Computational And Symbolic Checks

The following artifacts support reproducibility and sanity checking. They are
not substitutes for the proof above except where exact symbolic determinants
are recorded.

- `artifacts/box_model_checks.py` and
  `artifacts/box_model_checks_2026-05-30.log` verify the explicit `m=0` box
  violation and random box checks with fixed seed `20260530`.
- `artifacts/zonotope_midpoint_search.py` and
  `artifacts/zonotope_midpoint_search_2026-05-30.log` record fixed-seed
  zonotope midpoint searches.
- `artifacts/shared_zonotope_local_hessian_search.py` and
  `artifacts/shared_zonotope_local_hessian_search_2026-05-30.log` record a
  local Hessian sanity search in shared-direction zonotope cones.
- `artifacts/bivariate_counterexample_verification.py` and
  `artifacts/bivariate_counterexample_verification_2026-05-30.log` reproduce
  the exact Hessian determinants used in the bivariate counterexample artifact.

## Provenance

- User screenshot and approved goal in the Codex thread on 2026-05-30.
- `workspace/project/GOALS.yaml`
- `artifacts/n3_m2_lorentzian_bilinear_proof.md`
- `artifacts/bivariate_volume_polynomial_counterexamples.md`
- `artifacts/bivariate_counterexample_verification.py`
- `artifacts/bivariate_counterexample_verification_2026-05-30.log`
- `artifacts/box_model_checks.py`
- `artifacts/box_model_checks_2026-05-30.log`
- `artifacts/intermediate_cases_second_variation.md`
- `artifacts/quotient_concavity_literature_routes.md`
- `artifacts/branden_huh_2020_lorentzian_polynomials.pdf`
- `artifacts/branden_leake_2023_lorentzian_polynomials_on_cones.pdf`
- `artifacts/wang_2018_remark_alexandrov_fenchel.pdf`
- `artifacts/collins_2021_concave_elliptic_equations_generalized_khovanskii_teissier.pdf`
- `artifacts/kerner_nemethi_2017_generalized_fkg_compositions.pdf`
- `artifacts/lehmann_xiao_2017_correspondences_convex_complex_geometry.pdf`
- `reviews/logic_reviewer_revised_2026-05-30.json`
- `reviews/citation_checker_followup_2026-05-30.json`
- `reviews/archived_blocking_reviews_2026-05-30.md`

## Uncertainty

- The older blocking reviews apply to an obsolete attempted theorem
  (`1<=m<=n`) and are preserved in
  `reviews/archived_blocking_reviews_2026-05-30.md` as failed-review history.
- The construction of the negative examples is existential through Shephard's
  realization theorem; explicit vertex coordinates for the realizing polytopes
  are not produced in this workstream.
- The final theorem is reviewed as a working-paper result, not as a formalized
  Lean proof.

## Failed Explorations

- The hyperbolic volume polynomial route was rejected and recorded in
  `failures/hyperbolic_volume_polynomial_route.md`.
- The broad mixed-volume inverse quotient convexity black box was rejected by
  independent logic and citation reviews in `reviews/`.
- The Collins Hessian quotient analogy was recorded in
  `artifacts/quotient_concavity_literature_routes.md`; it explains why the
  false candidate theorem looked plausible but does not apply on the full
  convex-body cone.
