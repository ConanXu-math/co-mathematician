# Codex Co-Mathematician Project

This workspace is initialized and onboarding has begun. No mathematical research
workstream has started yet.

## Current Phase
research question formalization

## Research Question
Pending formal goal approval.

Current draft:

Determine, for integers `n >= 2` and `0 <= m <= n`, the necessary and
sufficient condition on `(n, m)` under which the functional

`F_{m,L}(K) = V(K[n-m], L[m]) / V(K[n-1], L)`

is Minkowski convex as a function of `K`, for every fixed convex body
`L in K^n`.

## Background

- User-provided context:
  The user supplied the definition of `F_{m,L}` via a screenshot and requested a
  strict proof of the full necessary-and-sufficient condition, with careful
  validation and no pseudo-proof.
- Key definitions:
  `K` varies over convex bodies in `K^n`; `L in K^n` is fixed; `V` denotes mixed
  volume; `K[j]` and `L[j]` denote repeated mixed-volume arguments. The target
  property is Minkowski convexity of `K -> F_{m,L}(K)`.
- Known references:
  User screenshot in the Codex thread on 2026-05-30 Asia/Shanghai. No source
  paper has yet been identified in the repository.
- Constraints:
  The argument must be fully rigorous, all important claims must have
  provenance, and any failed route or unresolved uncertainty must be preserved
  explicitly.

## Desired Output

A reviewed mathematical working paper that states the exact iff theorem,
contains a rigorous proof or rigorous counterexample-based elimination of false
cases, and records provenance, uncertainty, and failed explorations.

## Steering Notes

- User preferences:
  Explore the condition independently rather than asking the user to supply the
  missing iff conclusion. Verify strictly and avoid pseudo-proof.
- Decisions made:
  Onboarding started at 2026-05-29T16:46:51Z. The problem has been formalized as
  a classification question in `(n, m)`, but proof work has not started because
  goals are not yet approved.
- Open questions:
  Exact source reference for the theorem, precise convention for "Minkowski
  convex" to be used in the final paper, and whether the final proof will rely
  only on standard mixed-volume inequalities or also on explicit counterexample
  constructions.

## Operating Rule
Do not start workstreams until the user approves explicit goals in GOALS.yaml.

## Provenance Policy
Important claims must cite user input, literature, internal artifacts,
computation outputs, proof sketches, reviewer comments, or failed explorations.
