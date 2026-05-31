# Bivariate Volume-Polynomial Counterexamples For `n >= 4`

Date: 2026-05-30

## Purpose

This artifact gives counterexamples for every remaining intermediate case

`n >= 4`, `2 <= m <= n-1`.

It replaces the earlier working guess that all `m >= 1` might be positive.

## From Bivariate Volume Polynomials To The Functional

Let `P,Q` be full-dimensional convex bodies in `R^n`, and let

`f(x,y)=vol_n(xP+yQ)`.

Fix `L=Q` and restrict the variable body to the two-dimensional Minkowski cone

`K=xP+yQ`, with `x,y>0`.

By mixed-volume multilinearity,

`partial_y^j f(x,y) = n!/(n-j)! * V(K[n-j],Q[j])`.

Therefore

`F_{m,Q}(K) = ((n-m)!/(n-1)!) * (partial_y^m f)/(partial_y f)`.

The prefactor is positive, so convexity of `F_{m,Q}` on this cone is equivalent
to convexity of

`R_m(x,y) = (partial_y^m f)/(partial_y f)`.

## Realizing The Polynomials By Convex Bodies

For a bivariate homogeneous polynomial

`f(x,y)=sum_{k=0}^n c_k x^k y^(n-k)`,

the bivariate Lorentzian criterion is log-concavity of the normalized
coefficient sequence

`c_k / binom(n,k)`.

Branden-Huh record Shephard's construction: every bivariate Lorentzian
polynomial with rational coefficients is the volume polynomial of a pair of
`n`-dimensional convex polytopes with rational vertices.

In the extracted text artifact `branden_huh_2020_lorentzian_polynomials.txt`,
this appears on page 54: Shephard's construction shows that every polynomial
in `L^d_2 cap Q[w]` is the volume polynomial of a pair of `d`-dimensional
convex polytopes with rational vertices.

Thus any rational bivariate Lorentzian polynomial below is a genuine
mixed-volume counterexample.

## The Basic Family

For `N >= 4`, set

`f_N(x,y)=3(x+y)^N - 2x^N - 2y^N`.

Equivalently, the coefficients of `f_N` are

`1, 3*binom(N,1), ..., 3*binom(N,N-1), 1`.

The normalized coefficient sequence is

`1,3,3,...,3,1`,

which is log-concave. Hence `f_N` is bivariate Lorentzian and is realized as
`vol_N(xP+yQ)` for some full-dimensional rational polytopes `P,Q`.

## Base Counterexample For `m = 2`

Use `N=4` and

`f_4(x,y)=3(x+y)^4-2x^4-2y^4`.

For

`R_2=(partial_y^2 f_4)/(partial_y f_4)`,

the Hessian at `(x,y)=(2,1)` is

`[[85446, 114930], [114930, 134646]] / 493039`.

Its determinant is

`-3456/493039 < 0`.

Thus `R_2`, and hence `F_{2,Q}`, is not convex. This disproves the
intermediate case `n=4,m=2`.

## Base Counterexample For `m = 3`

Again use `N=4`. For

`R_3=(partial_y^3 f_4)/(partial_y f_4)`,

the Hessian at `(x,y)=(4,1)` is

`[[2257740, 3094524], [3094524, 4232340]] / 51895117`.

Its determinant is

`-147744/19356878641 < 0`.

Thus `F_{3,Q}` is not convex in dimension `4`.

## Base Counterexamples For `m >= 4`

Let `m >= 4` and take the base dimension

`N=m+1`.

For `f_N` above, put `d=N-1=m`. Since `partial_y^m f_N` is a positive
constant multiple of

`3(x+y)-2y`,

and `partial_y f_N` is a positive constant multiple of

`3(x+y)^d-2y^d`,

convexity would require the Hessian of

`R=(3s-2y)/(3s^d-2y^d)`, where `s=x+y`,

to be positive semidefinite.

At `(x,y)=(2,1)`, equivalently `(s,y)=(3,1)`, the Hessian determinant is

`2d^2(-6*3^(2d) + 49*3^d*d^2 - 98*3^d*d + 85*3^d - 54)`

divided by the positive denominator

`3(3*3^d-2)^4`.

For `d >= 4`, the numerator is negative. Indeed, it is enough to show

`6*3^d > 49d^2 - 98d + 85`.

This holds at `d=4`, where the difference is `9`, and the difference increases
with `d` because

`[6*3^(d+1) - (49(d+1)^2 - 98(d+1) + 85)]`

minus

`[6*3^d - (49d^2 - 98d + 85)]`

equals

`12*3^d - 98d > 0`

for `d >= 4`.

Thus `F_{m,Q}` is not convex in the base dimension `N=m+1` for every
`m >= 4`.

## Dimension-Lifting

Suppose a base counterexample has dimension `N` and volume polynomial
`f(x,y)=vol_N(xP+yQ)` for the desired `m`.

For any `r >= 0` and any `epsilon > 0`, define bodies in `R^(N+r)` by

`P_epsilon = P x [0,1]^r`,

`Q_epsilon = Q x [0,epsilon]^r`.

Then

`vol_(N+r)(xP_epsilon+yQ_epsilon) = f(x,y)(x+epsilon y)^r`.

As `epsilon -> 0+`, the quotient

`(partial_y^m [f(x,y)(x+epsilon y)^r]) /
 (partial_y [f(x,y)(x+epsilon y)^r])`

converges in `C^2` near the base point to

`(partial_y^m f)/(partial_y f)`.

The denominator is nonzero near each chosen base point, since at
`epsilon=0` it is `x^r partial_y f`, and `x>0`, `partial_y f>0` for volume
polynomials of full-dimensional bodies in positive directions.

Since the base Hessian determinant is strictly negative, it remains negative
for all sufficiently small positive `epsilon`. Both `P_epsilon` and
`Q_epsilon` are full-dimensional for `epsilon > 0`.

Therefore:

- The `n=4,m=2` base counterexample lifts to every `n >= 4` with `m=2`.
- The `n=4,m=3` base counterexample lifts to every `n >= 4` with `m=3`.
- For every `m >= 4`, the base counterexample in dimension `m+1` lifts to
  every `n >= m+1`.

Hence every intermediate case `n >= 4`, `2 <= m <= n-1`, fails.

## Provenance

- Branden-Huh, *Lorentzian polynomials*, Shephard realization statement for
  bivariate Lorentzian rational polynomials.
- Direct symbolic Hessian computations in this artifact.
- Mixed-volume derivative identity from the volume polynomial definition.

## Uncertainty

The construction relies on Shephard's realization theorem as quoted by
Branden-Huh. A reviewer should check the normalization convention, but all
normalization factors in `F_{m,Q}` are positive constants and do not affect
convexity or nonconvexity.
