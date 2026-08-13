# Proth proof evidence

`proth20-original-unit-0022.stdout.log` is the unmodified final unit output from
the discovery campaign. Its last completed record is the prime at `k=21952207`.

`proth20-reproduction.stdout.log` is the unmodified output of an isolated
one-candidate rerun using the preserved Proth20 0.9.1 adapter. Both outputs
identify witness `a = 3`.

`proth-certificate.json` binds the candidate, witness, source logs, independent
verification outputs, audit status, hashes, and source commit. It was copied
unchanged from the preserved private dossier.

The Proth20 executable is not included. Its SHA-256 is
`0c97e0e9f61c1e1aedb48ed7b7f5fa1f31343a9cb0cb167f4f4eb0e747dc2dfd`.

Proth20 did not emit a `RES64` for the prime line. The exact theorem residue
`N-1` is independently established by the scripts in
`../independent_verification/`.
