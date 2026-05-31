# Plan

## Objective

Classify the pairs `(n, m)`, with `n >= 2` and `0 <= m <= n`, for which

`F_{m,L}(K) = V(K[n-m], L[m]) / V(K[n-1], L)`

is Minkowski convex in `K` for every fixed full-dimensional convex body `L`.

## Current Classification

The revised necessary and sufficient condition is

`m = 1`, or `m = n`, or `(n,m) = (3,2)`.

## Work Items

1. Fix conventions for convex bodies, mixed-volume notation, and Minkowski
   convexity.
2. Verify the positive cases `m=1`, `m=n`, and `(n,m)=(3,2)`.
3. Produce an explicit counterexample for `m = 0`.
4. Produce bivariate volume-polynomial counterexamples for every
   intermediate case `n>=4`, `2<=m<=n-1`.
5. Record computational sanity checks separately from the proof.
6. Send the revised proof report to independent logic/provenance reviewers.

## Proof Route

- `m = 1`: immediate because the numerator equals the denominator.
- `m = n`: use mixed-volume Brunn-Minkowski concavity of
  `V(K[n-1],L)^(1/(n-1))`.
- `(n,m)=(3,2)`: use the Lorentzian bilinear form `q(X,Y)=V(X,Y,L)` and
  Cauchy-Schwarz on the primitive hyperplane.
- `m = 0`: use axis-aligned boxes and compute the mixed volumes exactly.
- `n>=4`, `2<=m<=n-1`: use bivariate Lorentzian volume polynomials, exact
  Hessian determinants, Shephard realization, and product lifting.

## Reviewer Focus

The reviewer should especially check the bivariate counterexample chain:
derivative normalization, Shephard realization, strict Hessian negativity, and
product lifting to higher dimensions.
