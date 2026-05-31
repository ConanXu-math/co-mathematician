# The Three-Dimensional Intermediate Case `n = 3, m = 2`

Date: 2026-05-30

## Purpose

This artifact proves the only intermediate case in dimension three:

`F_{2,L}(K) = V(K,L,L) / V(K,K,L)`

is Minkowski convex in `K` for every fixed full-dimensional convex body `L` in
`R^3`.

Together with the already proved endpoint cases `m = 1` and `m = 3`, and the
box counterexample for `m = 0`, this gives the full classification in dimension
`n = 3`.

## Bilinear Form

Fix `L` and define the symmetric bilinear form

`q(X,Y) = V(X,Y,L)`.

Mixed volume extends multilinearly to differences of support functions, so
directional second derivatives along Minkowski segments may be computed using
this form. The Alexandrov-Fenchel/Hodge-Riemann theorem implies that, on the
quotient by translations, `q` is Lorentzian: if `K` is full-dimensional and
`q(K,K)>0`, then `q` is non-positive on the primitive hyperplane

`H_K = { Z : q(K,Z) = 0 }`.

Equivalently, `-q` is positive semidefinite on `H_K`.

The precise provenance used here is Branden-Leake Lemma 2.3, which identifies
Alexandrov-Fenchel, Lorentzian signature, and primitive negative
semidefiniteness for a symmetric bilinear form, together with Branden-Leake
Corollary 6.6, which gives Alexandrov-Fenchel for convex bodies. See
`artifacts/branden_leake_2023_lorentzian_polynomials_on_cones.txt:230-285`
and `:1448-1472`.

## Second Derivative Calculation

Put

`B = q(K,K) = V(K,K,L)`,

`N = q(K,L) = V(K,L,L)`.

Both are positive. Let `Y` be an arbitrary virtual direction and decompose

`Y = aK + Z`, with `q(K,Z)=0`.

Then

`N' = q(Y,L) = aN + q(Z,L)`,

`N'' = 0`,

`B' = 2q(Y,K) = 2aB`,

`B'' = 2q(Y,Y) = 2a^2B + 2q(Z,Z)`.

For `Phi=N/B`, direct differentiation gives

`Phi'' = (N''B^2 - NB''B - 2N'B'B + 2N(B')^2) / B^3`.

Substituting the preceding formulas,

`B^3 Phi'' = 2B * (a^2 N B - 2a B q(Z,L) - N q(Z,Z))`.

Thus it remains to show that the quadratic

`a^2 N B - 2a B q(Z,L) - N q(Z,Z)`

is nonnegative for all real `a`.

## Lorentzian Cauchy-Schwarz Bound

Let

`C = q(L,L) = V(L,L,L)`

and project `L` to the primitive hyperplane:

`L_H = L - (N/B)K`.

Then `q(K,L_H)=0`, so `L_H in H_K`, and

`q(L_H,L_H) = C - N^2/B`.

By Alexandrov-Fenchel, `N^2 >= BC`, hence `q(L_H,L_H) <= 0`.

Since `Z` and `L_H` lie in `H_K`, and `-q` is positive semidefinite there, the
Cauchy-Schwarz inequality for `-q` gives

`q(Z,L)^2 = q(Z,L_H)^2`

`<= (-q(Z,Z))(-q(L_H,L_H))`

`= (-q(Z,Z))(N^2/B - C)`

`<= (-q(Z,Z))N^2/B`.

Equivalently,

`B q(Z,L)^2 <= -N^2 q(Z,Z)`.

The minimum of the quadratic in `a` is attained at `a=q(Z,L)/N`, and its value
is

`-B q(Z,L)^2/N - N q(Z,Z)`.

The preceding bound makes this minimum nonnegative. Therefore `Phi'' >= 0`
along every Minkowski segment on which the bodies remain full-dimensional.
This proves Minkowski convexity of `F_{2,L}` in dimension three.

## Provenance

- The second derivative formula is a direct calculation from mixed-volume
  multilinearity.
- The sign and Cauchy-Schwarz step uses the classical
  Alexandrov-Fenchel/Hodge-Riemann Lorentzian signature property for the form
  `q(X,Y)=V(X,Y,L)` in dimension three, sourced from Branden-Leake Lemma 2.3
  and Corollary 6.6.
- This proof was derived as a controlled test case for the general
  second-variation reduction in
  `artifacts/intermediate_cases_second_variation.md`.

## Remaining Uncertainty

This proof uses only a bilinear Lorentzian form. The general intermediate cases
`2 <= m <= n-1` require a higher-order analogue of the same projection estimate,
not just the usual primitive sign condition. That higher-order inequality is
not proved here.
