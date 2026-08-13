# Dated public-coverage audit

Two reproducible audit passes are represented here:

1. a preflight audit of odd `k=21909339..21989339` at `n=33326`, captured from
   `2026-08-12T20:59:35Z` to `2026-08-12T21:00:47Z`;
2. an exact post-result audit of `(k,n)=(21952207,33326)`, captured from
   `2026-08-13T01:44:25Z` to `2026-08-13T01:45:34Z`.

Each source manifest contains 79 records. The associated machine analyses report
no critical fetch failures, no manifest-integrity failures, and no possible
numeric overlap or relevant exact public hit in the captured sources.

The controlled conclusion is:

```text
PUBLICLY_UNCOVERED_CANDIDATE
```

Public wording:

> 21952207 × 2^33326 + 1 is a proven Proth prime. Independent verification
> was reproduced using distinct implementations. No prior exact public
> occurrence or documented public interval overlap was found in the sources
> audited on 13 August 2026.

This conclusion is deliberately narrower than “new” or “never computed”. Public
searches cannot exclude private, unpublished, unindexed, inaccessible, deleted,
or otherwise undiscoverable computations.

## Included evidence

- `range-target-and-queries.json`: deterministic range selection, seed, and
  sampled values.
- `range-source-manifest.json`: URLs, queries, timestamps, sizes, and hashes for
  the range audit.
- `range-machine-result.json`: parsed overlap checks and verdict.
- `exact-target-and-queries.json`: exact-result selection provenance.
- `exact-source-manifest.json`: URLs, queries, timestamps, sizes, and hashes for
  the exact audit.
- `exact-machine-result.json`: parsed exact-result checks and verdict.

The third-party response bodies are not redistributed because no uniform
redistribution license was established. Their retained SHA-256 values allow the
private captures to be matched exactly, while the URLs and queries document what
was consulted. Dynamic sources may no longer reproduce byte-for-byte when
fetched later; that is an explicit limitation of a dated web audit.
