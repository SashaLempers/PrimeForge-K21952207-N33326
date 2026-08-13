# Proven Proth prime — 21952207 × 2^33326 + 1

On 13 August 2026, PrimeForge found and proved the primality of
`21952207 × 2^33326 + 1`, a 10,040-digit Proth number.

Proth20 0.9.1 produced witness `a = 3`; an isolated Proth20 rerun reproduced
the result. PARI/GP 2.17.4 and CPython 3.12.13 independently reconstructed the
number and verified the exact congruence
`3^((N-1)/2) mod N = N-1`.

A dated public-coverage audit found no prior exact public occurrence or
documented public interval overlap in the sources consulted. This does not
establish that no private, unpublished, unindexed, inaccessible, or deleted
prior computation exists.

The attached deterministic ZIP contains the compact evidence dossier,
independent-verification scripts and outputs, audit manifests, commands,
software versions, source commits, and SHA-256 checksums. No third-party binary,
private repository history, credential, or private machine path is included.

The archive SHA-256 is supplied in the separate `SHA256SUMS.txt` attachment.

Zenodo DOI: pending publication.
