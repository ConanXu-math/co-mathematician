# Literature Routes For The Remaining Quotient-Convexity Gap

Date: 2026-05-30

## Purpose

This artifact records a now-superseded proof route for the formerly open range

`n >= 4`, `2 <= m <= n-1`.

This artifact records literature statements that are close to the needed
quotient convexity, and states explicitly why they do or do not yet close the
gap.

Later in the workstream, `artifacts/bivariate_volume_polynomial_counterexamples.md`
showed that this range is not open-positive but false: all these intermediate
cases fail.

## Target Reformulation

Let

`B(K)=V(K[n-1],L)`, `A(K)=V(K[n-m],L[m])`, `r=m-1`.

The desired convexity of `A/B` would follow if

`G(K) = (B(K)/A(K))^(1/r)`

were Minkowski concave. Indeed, `A/B = G^(-r)`, and the reciprocal of a
positive concave function is convex; raising a positive convex function to a
power `r >= 1` preserves convexity.

## Collins Hessian Quotient Concavity

T. C. Collins, *Concave elliptic equations and generalized
Khovanskii-Teissier inequalities*, arXiv:1903.10898.

Corollary 2.20 states that, on the solvable set for a complex Hessian quotient
equation,

`[alpha] -> (omega^(n-k).alpha^k / omega^(n-l).alpha^l)^(1/(k-l))`

is concave. Collins then observes that

`[alpha] -> omega^(n-l).alpha^l / omega^(n-k).alpha^k`

is convex on that same solvable set.

With the substitution

`k=n-1`, `l=n-m`, `omega=L`, `alpha=K`,

this is formally exactly the desired quotient:

`omega^(n-l).alpha^l / omega^(n-k).alpha^k`

`= L[m].K[n-m] / (L.K[n-1])`.

### Limitation

Collins' theorem applies on a PDE-defined solvable set. The workstream has not
proved that the corresponding solvable set is the entire cone of convex bodies,
nor that the Kähler argument transfers to arbitrary convex bodies without an
extra assumption. Thus this is a strong model theorem and proof route, but not
yet a proof of the present problem.

## Lehmann-Xiao Reverse Khovanskii-Teissier Inequality

B. Lehmann and J. Xiao, *Correspondences between convex geometry and complex
geometry*, arXiv:1709.00611.

Theorem 5.9 proves the convex-body inequality

`V(K[k],L[n-k]) V(L[k],M[n-k]) >= (k!(n-k)!/n!) vol(L) V(K[k],M[n-k])`.

Its proof uses mass transport and mixed discriminants, matching the analytic
style that may be needed here.

### Limitation

The theorem compares mixed volumes of positive convex bodies. The
second-variation criterion for the current quotient requires estimates for
virtual directions `Z` in the primitive hyperplane, including terms such as
`D_Z^2 A`, `D_Z A`, and `D_Z^2 B`. Theorem 5.9 does not directly provide that
signed local inequality.

## Kerner-Nemethi Generalized FKG Inequality

D. Kerner and A. Nemethi, *A generalized FKG-inequality for compositions*,
arXiv:1412.8200.

Corollary 4.1 gives corrected Jensen/FKG-type inequalities for arrays of mixed
volumes over composition posets. The paper explicitly notes that naive
Jensen-type inequalities for mixed volumes fail in general and cites Burda's
counterexample.

### Limitation

These inequalities control averages of positive mixed-volume coefficients.
They do not directly imply convexity of `K -> A(K)/B(K)` along arbitrary
Minkowski segments, nor the signed primitive second-variation inequality.

## Current Conclusion

This route is now understood as explaining a plausible but false analogy.
The checked sources do not prove full-cone convexity, and the bivariate
counterexamples show that such full-cone convexity cannot be true in general.

The failed route was:

1. Prove a convex-body analogue of Collins' Hessian quotient concavity for the
   full convex-body cone.
2. Or prove directly the strengthened local Hodge-Riemann inequality recorded
   in `artifacts/intermediate_cases_second_variation.md`.
3. Find a counterexample in `n >= 4` showing the formal Collins analogy is too
   optimistic.

The third alternative occurred; see
`artifacts/bivariate_volume_polynomial_counterexamples.md`.
