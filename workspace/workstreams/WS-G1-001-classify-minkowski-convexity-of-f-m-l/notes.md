# Notes

## 2026-05-30

- The project goals G1 and G2 were approved by the user.
- Proof workstream `WS-G1-001-classify-minkowski-convexity-of-f-m-l` was created.
- Randomized tests on axis-aligned boxes support the classification `m >= 1`.
- A fully explicit counterexample for `m = 0` is available for every `n >= 2`:
  take `L` to be the unit cube, and compare boxes with side lengths
  `(R,1,1,...,1)` and `(1,R,1,...,1)`.
- Literature artifacts downloaded so far:
  `bauschke_guler_lewis_sendov_2001_hyperbolic_polynomials_and_convex_analysis.pdf`,
  `huh_volume_polynomials.pdf`,
  `wang_2018_remark_alexandrov_fenchel.pdf`,
  `lehmann_xiao_2017_correspondences_convex_complex_geometry.pdf`,
  and `fradelizi_giannopoulos_meyer_2003_some_inequalities_about_mixed_volumes.pdf`.
- Important uncertainty:
  The positive-case proof route should not be marked complete until an
  independent reviewer checks that the quotient convexity theorem used below is
  exactly valid for the mixed-volume functional in this problem.
- Independent logic and citation reviews rejected the broad mixed-volume
  inverse quotient convexity statement as unsupported. The report has been
  downgraded to verified cases plus an explicit intermediate-case proof gap.
- Reproducibility fix:
  `artifacts/box_model_checks.py` now uses fixed random seed `20260530`, with
  output saved in `artifacts/box_model_checks_2026-05-30.log`.
- Additional computation:
  `artifacts/zonotope_midpoint_search.py` tests random zonotopes with fixed
  seed `20260531`; the saved log reports no midpoint-convexity violations for
  the tested `m >= 2` cases in dimensions 4 and 5.
- Additional local computation:
  `artifacts/shared_zonotope_local_hessian_search.py` tests Hessian positivity
  of the quotient in fixed-direction zonotope length cones with seed
  `2026053003`; the saved log reports no negative Hessian eigenvalues in the
  tested intermediate cases for `n=4,5`.
- Verified positive cases currently include `m = 1` and `m = n`. The case
  `m = n` follows from the Brunn-Minkowski concavity of
  `V(K[n-1],L)^{1/(n-1)}` and convexity of reciprocal positive powers.
- Major update:
  the previous candidate `1<=m<=n` is false. The revised classification is
  `m=1`, or `m=n`, or the exceptional case `(n,m)=(3,2)`.
- New negative proof for intermediate cases:
  `artifacts/bivariate_volume_polynomial_counterexamples.md` constructs
  bivariate Lorentzian volume-polynomial counterexamples for every
  `n>=4`, `2<=m<=n-1`, using Shephard realization and product lifting.
- Exact symbolic verification:
  `artifacts/bivariate_counterexample_verification.py` reproduces the base
  Hessian determinants and the general determinant formula for the
  `m=n-1` base family.
- The artifact `artifacts/intermediate_cases_second_variation.md` reduces the
  intermediate proof gap to a precise local inequality:
  for `B(K)=V(K[n-1],L)`, `A=D_L^{m-1}B`, and every `B`-primitive direction
  `Z`, it is enough to prove
  `D_Z^2 A/A - (r/(r+1))(D_Z A/A)^2 >= D_Z^2 B/B`,
  where `r=m-1`.
- New verified special case:
  `artifacts/n3_m2_lorentzian_bilinear_proof.md` proves the only
  three-dimensional intermediate case `n=3,m=2`. The proof uses the
  Lorentzian signature of `q(X,Y)=V(X,Y,L)`, primitive decomposition
  `Y=aK+Z`, and Cauchy-Schwarz for `-q` on the primitive hyperplane.
- Current proof scope:
  `m=0` fails for all `n>=2`; `m=1` and `m=n` hold for all `n>=2`; `(n,m)=(3,2)`
  holds; and all intermediate cases in dimensions `n>=4` fail. A fresh
  independent reviewer is still required before completion.
- Citation review update:
  `reviews/citation_checker_revised_blocking_2026-05-30.json` approved the
  Branden-Huh/Shephard counterexample provenance but blocked the report until
  exact positive-case sources were added. The report now cites Wang Theorem 2.7
  and Lemma 2.5 for the `m=n` endpoint, and Branden-Leake Lemma 2.3 plus
  Corollary 6.6 for the Lorentzian signature used in `n=3,m=2`.
- Literature route update:
  `artifacts/quotient_concavity_literature_routes.md` records that Collins'
  Hessian quotient concavity has the exact formal quotient needed after
  substituting `k=n-1`, `l=n-m`, but is currently limited to a PDE solvable set.
  Lehmann-Xiao reverse Khovanskii-Teissier and Kerner-Nemethi generalized FKG
  provide nearby inequalities but do not yet imply the signed primitive
  second-variation inequality.
  The bivariate counterexamples explain why the Collins analogy cannot hold on
  the full convex-body cone.
