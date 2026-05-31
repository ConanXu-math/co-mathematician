# Failed Exploration: Treating the Volume Polynomial as Hyperbolic

## Attempt

Try to prove the positive cases by considering the volume polynomial

`p(K) = vol(K)`

on a formal vector space of convex bodies and applying hyperbolic-polynomial
convexity results to the quotient of directional derivatives in the direction
`L`.

## Why This Was Rejected

This route would require the relevant volume polynomial to be hyperbolic in the
needed sense. That is not available for arbitrary convex bodies. The safer
framework is Lorentzian/Hodge-Riemann or Alexandrov-Fenchel theory for mixed
volumes, not characteristic-root convexity for a globally hyperbolic volume
polynomial.

The issue is not cosmetic: relying on a hyperbolicity statement not known to
hold for arbitrary convex bodies would make the proof circular or false.

## Replacement Route

Use an Alexandrov-Fenchel/Hodge-Riemann mixed-volume quotient convexity input
for the positive cases, and verify the source-to-statement match independently.

## Provenance

- `artifacts/bauschke_guler_lewis_sendov_2001_hyperbolic_polynomials_and_convex_analysis.pdf`
- `artifacts/huh_volume_polynomials.pdf`
- Internal reasoning during proof workstream on 2026-05-30.

## Uncertainty

This failure note does not itself prove the positive cases; it only rules out a
tempting but insufficient proof strategy.
