# Proven Proth prime: 21952207 × 2^33326 + 1

On 13 August 2026, PrimeForge found and proved the primality of

    21952207 × 2^33326 + 1

The result was independently verified using distinct implementations.

A dated public-coverage audit found no prior exact public occurrence or
documented public interval overlap in the sources consulted.

This does not establish that no private or unpublished prior computation exists.

This repository is a minimal, audited public export of the discovery evidence.
It does not expose the private PrimeForge repository or redistribute the
third-party executables used during discovery and verification.

## Result

- Form: `k × 2^n + 1`
- `k = 21952207`
- `n = 33326`
- Decimal digits: `10040`
- Proth witness: `a = 3`
- Exact congruence: `3^((N-1)/2) mod N = N-1`
- Discovery UTC: `2026-08-13T01:32:17Z`
- PrimeForge engine commit: `ed270719caca06c7f3780585070519b35ea9af4a`
- Private evidence-report commit: `c7a1a3812ec03a0f3e7be08549816c847ffee3ba`

The full decimal expansion is in
[`NUMBER.txt`](discoveries/K21952207_N33326/NUMBER.txt). The evidence index and
reproduction instructions are in the
[`discovery dossier`](discoveries/K21952207_N33326/README.md).

## Verification summary

Proth20 0.9.1 reported the number prime with witness `a = 3`, and an isolated
second Proth20 run reproduced that verdict. PARI/GP 2.17.4 and CPython 3.12.13
then independently reconstructed the integer and evaluated the exact Proth
congruence. Both returned `N-1` as the modular residue and a
`PROVEN_PRIME` verdict.

Proth20 did not emit a `RES64` field for the prime result. No `RES64` value is
therefore claimed or reconstructed.

## Public-coverage statement

The original range audit and the exact post-result audit each captured 79 public
source responses. The exact audit ran from `2026-08-13T01:44:25Z` through
`2026-08-13T01:45:34Z`. No prior exact public occurrence or documented public
interval overlap was found in the sources audited on 13 August 2026.

The controlled assessment is `PUBLICLY_UNCOVERED_CANDIDATE`, not a claim that
the number had never been computed. Private, unpublished, unindexed, deleted,
inaccessible, or otherwise undiscoverable work cannot be excluded.

## Quick verification

With Python 3.11 or newer:

```console
python scripts/validate_publication.py --full
python scripts/build_release.py
```

The full verification performs an exact 10,040-digit modular exponentiation and
can take tens of seconds. PARI/GP reproduction is documented separately because
the PARI binary is not redistributed.

## Release and citation

- Version: `1.0.0`
- Immutable tag: `discovery-k21952207-n33326-2026-08-13`
- Zenodo DOI: [`10.5281/zenodo.21916421`](https://doi.org/10.5281/zenodo.21916421)
- Citation metadata: [`CITATION.cff`](CITATION.cff)

See [`RIGHTS.md`](RIGHTS.md) before redistributing material from this export.
