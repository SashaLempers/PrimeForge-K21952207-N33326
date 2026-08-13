# Discovery report: 21952207 × 2^33326 + 1

## Result

PrimeForge found the Proth number `N = 21952207 × 2^33326 + 1` during a
controlled search. The integer has exactly 10,040 decimal digits. Detection was
recorded at `2026-08-13T01:32:17Z`.

The following statements are supported by the files in this dossier:

1. `N` is mathematically proven prime by Proth's theorem with witness `a = 3`.
2. An isolated Proth20 rerun reproduced the proof verdict.
3. PARI/GP 2.17.4 independently computed
   `3^((N-1)/2) mod N = N-1` and `kronecker(3,N) = -1`.
4. CPython 3.12.13 independently computed the same exact modular congruence.
5. A dated audit found no prior exact public occurrence or documented public
   interval overlap in the 79 sources consulted on 13 August 2026.

The fifth statement is a bounded public-evidence statement. It does not prove
that no private, unpublished, unindexed, inaccessible, or deleted computation
exists. No “world first”, “first ever”, or globally unexplored claim is made.

## Discovery campaign

```text
campaign_id=sha256:36e0132df476ff8daebae815c3576d195fafaab05775b31b8a81a05842197cce
family=k*2^n+1
n=33326
k_min=21909339
k_max=21989339
k_step=2
sieve_bound=65521
sieve_survivors=4012
completed_results=2161
checkpoint_status=PRIME_FOUND
prime_k=21952207
```

The range was generated reproducibly with the documented `SHA256_WINDOW_V1`
selection algorithm. Its seed and SHA-256 are preserved in the range target
record under `novelty_audit/`. Before the campaign, three full-size survivors
agreed between Proth20 and PARI/GP, and a two-record interruption followed by a
one-record resume completed without gaps or duplicates.

The final campaign integrity record reports an exact prefix match between the
4,012 sieve survivors and the 2,161 completed records, with zero missing,
duplicate, or invalid records in that prefix. It records exactly one proven
prime and `next_k=21952209`.

## Proof

The Proth conditions hold: `k` is positive and odd, and
`21952207 < 2^33326`. Proth20 0.9.1 reported:

```text
21952207 * 2^33326 + 1 is prime, a = 3
```

An isolated second run using the preserved executable returned exit code zero
and the same witness and verdict. The executable itself is not redistributed;
its SHA-256 is recorded in `SOFTWARE_VERSIONS.json`.

Proth20 emitted no `RES64` value for the prime line. The exact theorem residue
is nevertheless available from both independent calculations: it is `N-1`.

## Independent verification

PARI/GP 2.17.4 and CPython 3.12.13 each reconstructed `N` directly from `k` and
`n`, then performed arbitrary-precision modular exponentiation. Their scripts
and unmodified standard output are included. They both report 10,040 digits,
the exact Proth congruence, and a `PROVEN_PRIME` verdict.

A supplemental general FLINT primality attempt was stopped after its working set
reached 36,851,220,480 bytes and available RAM fell below the predeclared 8 GiB
gate. It produced no verdict and is not counted as verification.

## Public-coverage audit

The range preflight audit ran from `2026-08-12T20:59:35Z` to
`2026-08-12T21:00:47Z`. The exact post-result audit ran from
`2026-08-13T01:44:25Z` to `2026-08-13T01:45:34Z`. Each manifest contains 79
source records. The machine analyses report zero critical fetch failures, zero
manifest-integrity failures, and zero possible overlaps or relevant exact hits.

The audited source classes include EST Proth; FermatSearch done, running, live
range, and merged views; PrimeGrid PPS/PPSE; PrimePages/T5K; exact web queries;
GitHub; GitLab; OEIS; arXiv; Archive.org; Crossref; DataCite; OpenAlex; Zenodo;
and Figshare. The manifest supplies the exact URLs, queries, retrieval times,
sizes, and hashes.

Known limitations include:

- public searches cannot reveal private or unindexed computations;
- GitHub provides no global search over every release-asset payload;
- T5K is not exhaustive for primes of this size;
- the FermatSearch views share an operator database and do not remove the
  limitation of the displayed source update date;
- raw third-party responses are retained privately but are not redistributed in
  this export because a uniform redistribution license was not established.

## Environment and provenance

Discovery used Proth20 0.9.1 through the PrimeForge batch adapter on an NVIDIA
GeForce RTX 5080 via OpenCL 3.0 CUDA, NVIDIA driver 610.74. The source engine
commit was `ed270719caca06c7f3780585070519b35ea9af4a`; the audited private report
was committed as `c7a1a3812ec03a0f3e7be08549816c847ffee3ba` after local tests and
green Windows/Linux CI.

Detailed versions, commands, raw evidence, and hashes are linked from the
directory [`README.md`](README.md).

## Publication

The public evidence deposit is identified by Zenodo DOI
[`10.5281/zenodo.21916421`](https://doi.org/10.5281/zenodo.21916421). The DOI
record contains the deterministic evidence archive and its separate SHA-256
checksum file.
