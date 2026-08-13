# Evidence dossier

This directory contains the compact public evidence for the proven Proth prime

    21952207 × 2^33326 + 1.

## Evidence map

- [`NUMBER.txt`](NUMBER.txt): exact 10,040-digit decimal integer.
- [`FORM.txt`](FORM.txt): unambiguous parameters and theorem witness.
- [`DISCOVERY_REPORT.md`](DISCOVERY_REPORT.md): controlled scientific report.
- [`COMMANDS.md`](COMMANDS.md): reproduction and original campaign commands.
- [`SOFTWARE_VERSIONS.json`](SOFTWARE_VERSIONS.json): versions, platform facts,
  executable hashes, and source commits.
- [`proof/`](proof/): Proth20 original and isolated reproduction output plus the
  machine-readable certificate.
- [`independent_verification/`](independent_verification/): exact PARI/GP and
  CPython scripts and their captured outputs.
- [`novelty_audit/`](novelty_audit/): range and exact-result public-coverage
  manifests, machine verdicts, and limitations.
- [`raw/`](raw/): minimal raw campaign state, result prefix, sieve survivors,
  integrity report, validation report, and telemetry summary.
- `SHA256SUMS.txt`: generated SHA-256 list for every other file in this dossier.

## Controlled statuses

```text
primality_status=PROVEN_PRIME
verification_status=INDEPENDENTLY_VERIFIED
novelty_status=DUE_DILIGENCE_COMPLETE
public_novelty_assessment=PUBLICLY_UNCOVERED_CANDIDATE
new_prime_claim=NOT_MADE
```

`PUBLICLY_UNCOVERED_CANDIDATE` means only that no prior exact public occurrence
or documented public interval overlap was found in the dated sources consulted.
It does not establish the absence of private or unpublished prior computation.

## Reproduce the proof

Run the public validator from the repository root:

```console
python scripts/validate_publication.py --full
```

The validator checks the decimal expansion, the algebraic form, the witness,
the exact Proth congruence, key campaign invariants, every dossier SHA-256, local
Markdown links, and publication-safety patterns. For a direct PARI/GP run:

```console
gp -q discoveries/K21952207_N33326/independent_verification/pari/verify.gp
```

Expected terminal fields are `PROTH_CONGRUENCE=1`, `KRONECKER=-1`, and
`PARI_PROTH_VERDICT=PROVEN_PRIME`.

## Archive

`python scripts/build_release.py` creates a deterministic ZIP under `release/`
and a separate SHA-256 file. The ZIP entries are lexicographically ordered,
have fixed timestamps and permissions, and exclude `.git`, release output,
third-party binaries, and private artifacts.
