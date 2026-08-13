#!/usr/bin/env python3
"""Build the deterministic PrimeForge discovery release archive."""

from __future__ import annotations

import hashlib
import os
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOSSIER = ROOT / "discoveries" / "K21952207_N33326"
RELEASE = ROOT / "release"
ARCHIVE_NAME = "PrimeForge-K21952207-N33326-artifacts.zip"
PREFIX = "PrimeForge-K21952207-N33326"
FIXED_TIMESTAMP = (2026, 8, 13, 0, 0, 0)
TOP_FILES = [
    "README.md",
    "CITATION.cff",
    "RIGHTS.md",
    "LICENSE",
    "RELEASE_NOTES.md",
    "ZENODO_DEPOSIT.md",
    "ZENODO_METADATA_DRAFT.json",
]
TOP_DIRS = ["discoveries", "scripts"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def update_dossier_hashes() -> None:
    target = DOSSIER / "SHA256SUMS.txt"
    files = sorted(
        (path for path in DOSSIER.rglob("*") if path.is_file() and path != target),
        key=lambda path: path.relative_to(DOSSIER).as_posix().encode("utf-8"),
    )
    content = "".join(
        f"{sha256(path)}  {path.relative_to(DOSSIER).as_posix()}\n" for path in files
    )
    target.write_text(content, encoding="utf-8", newline="\n")


def selected_files() -> list[Path]:
    files = [ROOT / name for name in TOP_FILES]
    for directory in TOP_DIRS:
        files.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix().encode("utf-8"))


def build_zip(destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in selected_files():
            relative = path.relative_to(ROOT).as_posix()
            information = zipfile.ZipInfo(f"{PREFIX}/{relative}", FIXED_TIMESTAMP)
            information.compress_type = zipfile.ZIP_DEFLATED
            information.create_system = 3
            information.external_attr = (0o100644 << 16)
            archive.writestr(information, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> int:
    os.environ.setdefault("SOURCE_DATE_EPOCH", "1786579200")
    update_dossier_hashes()
    RELEASE.mkdir(exist_ok=True)
    archive_path = RELEASE / ARCHIVE_NAME
    temporary = RELEASE / f".{ARCHIVE_NAME}.tmp"
    if temporary.exists():
        temporary.unlink()
    build_zip(temporary)
    shutil.move(str(temporary), archive_path)
    digest = sha256(archive_path)
    (RELEASE / "SHA256SUMS.txt").write_text(
        f"{digest}  {ARCHIVE_NAME}\n", encoding="utf-8", newline="\n"
    )
    print(f"archive={archive_path}")
    print(f"archive_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
