# Zenodo deposit plan

This file records the reviewed metadata for the public Zenodo deposit. The
machine-readable companion is `ZENODO_METADATA_DRAFT.json`.

## Resource type

`Dataset` is selected because the deposit's primary object is a compact
scientific evidence dataset: a 10,040-digit integer, proof logs, independent
verification scripts and outputs, campaign records, public-coverage manifests,
and checksums. It is not a release of the complete PrimeForge software.

## Rights

Zenodo requires at least one license or rights statement and supports mixed and
custom rights. A blanket Creative Commons license is not assigned because the
original PrimeForge code, generated evidence, and factual third-party tool
output do not share one pre-existing license.

Use two entries in the Zenodo rights editor:

1. `Apache License 2.0` for `scripts/` and `.github/workflows/validate.yml` only.
2. A custom statement titled `PrimeForge discovery evidence rights statement`
   with this description:

   > Discovery records, reports, logs, numerical output, manifests, and
   > verification data are made publicly accessible for scientific inspection
   > and reproducibility. No broader copyright license is granted unless a file
   > says otherwise. Facts and mathematical results may have different legal
   > treatment depending on jurisdiction. Third-party programs and captured web
   > response bodies are not included.

This records the actual mixed-rights state without inventing an ORCID,
affiliation, or blanket data license.

## DOI sequence

Zenodo reserved `10.5281/zenodo.21916421` for this deposit on 13 August 2026.
The immutable GitHub tag and archive were prepared before reservation and do
not contain the DOI. The default branch and editable release description may
reference the reserved DOI; the tag and released archive must not be rewritten
or replaced.
