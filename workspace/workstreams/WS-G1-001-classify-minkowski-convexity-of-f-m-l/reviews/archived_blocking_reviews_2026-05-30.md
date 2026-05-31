# Archived Blocking Reviews

Date: 2026-05-30

The following earlier blocking reviews applied to an obsolete report whose
candidate theorem was `1 <= m <= n`:

- `logic_reviewer_blocking_2026-05-30.json`

```json
{
  "approved": false,
  "severity": "blocking",
  "issue_type": "logic",
  "reviewer": "logic_reviewer",
  "comment": "The blocking gap was the positive-case step in the obsolete report: the asserted black-box theorem that K -> V(K[i],L[n-i]) / V(K[j],L[n-j]) is Minkowski convex for all 0 <= i < j <= n-1 was not established from cited material. The m=0 box counterexample algebra checked out.",
  "suggested_fix": "Do not claim the full positive classification from the unsupported inverse quotient convexity theorem.",
  "checked_artifacts": [
    "report.md",
    "failures/hyperbolic_volume_polynomial_route.md",
    "artifacts/box_model_checks.py"
  ]
}
```

- `citation_checker_blocking_2026-05-30.json`

```json
{
  "approved": false,
  "severity": "blocking",
  "issue_type": "citation",
  "reviewer": "citation_checker",
  "comment": "The positive-case statement in the obsolete report was not source-supported as written. The cited sources did not prove the asserted full inverse mixed-volume quotient convexity statement. The m=0 counterexample was adequately self-contained.",
  "suggested_fix": "Replace the positive-case claim with a theorem actually cited or add a source/artifact proving the full mixed-volume quotient convexity statement.",
  "checked_artifacts": [
    "report.md",
    "artifacts/wang_2018_remark_alexandrov_fenchel.pdf",
    "artifacts/lehmann_xiao_2017_correspondences_convex_complex_geometry.pdf",
    "artifacts/fradelizi_giannopoulos_meyer_2003_some_inequalities_about_mixed_volumes.pdf",
    "artifacts/huh_volume_polynomials.pdf",
    "artifacts/bauschke_guler_lewis_sendov_2001_hyperbolic_polynomials_and_convex_analysis.pdf",
    "artifacts/box_model_checks.py"
  ]
}
```

- `citation_checker_revised_blocking_2026-05-30.json`

```json
{
  "approved": false,
  "severity": "blocking",
  "issue_type": "missing_provenance",
  "reviewer": "citation_checker_revised_2026-05-30",
  "comment": "The revised negative-case provenance chain was materially improved, and the Branden-Huh/Shephard step was within scope. The report still had a blocking provenance gap on the positive cases because the exact sources for the m=n mixed-volume Brunn-Minkowski input and the n=3,m=2 Lorentzian signature input were not named.",
  "suggested_fix": "Add exact local source references and theorem locations for the m=n endpoint and the n=3,m=2 Lorentzian signature input.",
  "checked_artifacts": [
    "report.md",
    "artifacts/bivariate_volume_polynomial_counterexamples.md",
    "artifacts/n3_m2_lorentzian_bilinear_proof.md",
    "artifacts/branden_huh_2020_lorentzian_polynomials.txt",
    "artifacts/wang_2018_remark_alexandrov_fenchel.txt"
  ]
}
```

They are preserved as durable research history but are superseded by:

- `logic_reviewer_revised_2026-05-30.json`
- `citation_checker_followup_2026-05-30.json`

The revised theorem is:

`F_{m,L}` is universally Minkowski convex exactly for `m=1`, `m=n`, or
`(n,m)=(3,2)`.

This archive note exists because the harness treats any `*.json` review with
`severity: blocking` as an active completion blocker. The original JSON reviews
are therefore moved out of the active `reviews/` glob while their contents
remain preserved in this note and in the project message log.
