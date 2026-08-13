#!/usr/bin/env python3
"""Validate the public PrimeForge discovery dossier."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(20_000)


ROOT = Path(__file__).resolve().parent.parent
DOSSIER = ROOT / "discoveries" / "K21952207_N33326"
K = 21_952_207
EXPONENT = 33_326
WITNESS = 3


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_json(relative: str) -> object:
    with (DOSSIER / relative).open("r", encoding="utf-8") as stream:
        return json.load(stream)


def validate_number() -> None:
    decimal = (DOSSIER / "NUMBER.txt").read_text(encoding="ascii").strip()
    require(re.fullmatch(r"[1-9][0-9]*", decimal) is not None, "NUMBER.txt is not canonical decimal")
    require(len(decimal) == 10_040, "unexpected decimal digit count")
    number = K * (1 << EXPONENT) + 1
    require(str(number) == decimal, "NUMBER.txt does not equal k*2^n+1")
    require(K > 0 and K % 2 == 1 and K < (1 << EXPONENT), "Proth conditions failed")
    require(hashlib.sha256(decimal.encode("ascii")).hexdigest() ==
            "039377ed4a52e5d5a6ed1b988856d74141999c2b0160abc5065274a994397155",
            "candidate decimal SHA-256 mismatch")


def validate_metadata() -> None:
    certificate = load_json("proof/proth-certificate.json")
    candidate = certificate["candidate"]
    statuses = certificate["statuses"]
    require(candidate["k"] == str(K), "certificate k mismatch")
    require(candidate["n"] == str(EXPONENT), "certificate n mismatch")
    require(candidate["decimal_digits"] == 10_040, "certificate digit mismatch")
    require(certificate["theorem"]["witness_a"] == str(WITNESS), "certificate witness mismatch")
    require(certificate["theorem"]["verified_congruence"] is True,
            "certificate does not record the congruence")
    require(statuses == {
        "primality_status": "PROVEN_PRIME",
        "verification_status": "INDEPENDENTLY_VERIFIED",
        "novelty_status": "DUE_DILIGENCE_COMPLETE",
        "public_novelty_assessment": "PUBLICLY_UNCOVERED_CANDIDATE",
        "new_prime_claim": "NOT_MADE",
    }, "controlled status mismatch")

    campaign = load_json("raw/campaign.json")
    checkpoint = load_json("raw/checkpoint.json")
    integrity = load_json("raw/campaign-integrity.json")
    require(campaign["campaign_id"] == checkpoint["campaign_id"] == integrity["campaign_id"],
            "campaign identity mismatch")
    require(checkpoint["campaign_status"] == "PRIME_FOUND", "checkpoint is not PRIME_FOUND")
    require(checkpoint["proven_prime_k"] == K, "checkpoint prime k mismatch")
    require(integrity["exact_prefix_match"] is True, "campaign prefix mismatch")
    require(integrity["sequence_difference_count"] == 0, "campaign sequence difference")
    require(integrity["duplicate_k_count"] == 0, "duplicate campaign record")
    require(integrity["invalid_record_count"] == 0, "invalid campaign record")
    require(integrity["proven_prime_count"] == 1, "unexpected prime count")

    exact_manifest = load_json("novelty_audit/exact-source-manifest.json")
    exact_result = load_json("novelty_audit/exact-machine-result.json")
    require(exact_manifest["source_count"] == 79, "exact audit source count mismatch")
    require(exact_result["coverage_verdict"] == "PUBLICLY_UNCOVERED_CANDIDATE",
            "exact audit verdict mismatch")
    require(exact_result["numeric_overlap_checks"]["total_possible_overlaps_or_matches"] == 0,
            "exact audit records an overlap or match")


def validate_hashes() -> None:
    checksum_path = DOSSIER / "SHA256SUMS.txt"
    require(checksum_path.is_file(), "SHA256SUMS.txt is missing")
    listed: set[str] = set()
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        digest, relative = line.split("  ", 1)
        path = DOSSIER / Path(relative)
        require(path.is_file(), f"hashed file is missing: {relative}")
        require(sha256(path) == digest, f"SHA-256 mismatch: {relative}")
        listed.add(relative)
    actual = {
        path.relative_to(DOSSIER).as_posix()
        for path in DOSSIER.rglob("*")
        if path.is_file() and path.name != "SHA256SUMS.txt"
    }
    require(listed == actual, "SHA256SUMS.txt does not cover the exact dossier file set")


def validate_links() -> None:
    pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        for target in pattern.findall(source.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            require((source.parent / relative).resolve().exists(),
                    f"broken relative link in {source.relative_to(ROOT)}: {target}")


def validate_publication_safety() -> None:
    windows_separator = chr(92)
    private_home = "C:" + windows_separator + "Users" + windows_separator + "sashack"
    private_home_forward = "/".join(("C:", "Users", "sashack"))
    appdata_windows = windows_separator + "AppData" + windows_separator
    appdata_forward = "/" + "AppData" + "/"
    forbidden = {
        re.escape(private_home): "private Windows home path",
        re.escape(private_home_forward): "private Windows home path",
        f"{re.escape(appdata_windows)}|{re.escape(appdata_forward)}": "AppData path",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----": "private key",
        r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b": "GitHub token",
        r"\bgithub_pat_[A-Za-z0-9_]{20,}\b": "GitHub fine-grained token",
        r"\b(?:password|passwd)\s*[:=]\s*[^\s<]+": "password assignment",
        r"\b(?:access_token|refresh_token|session_id)\s*[:=]\s*[^\s<]+": "credential assignment",
        r"\b(?:10\.(?:[0-9]{1,3}\.){2}|127\.(?:[0-9]{1,3}\.){2}|"
        r"169\.254\.[0-9]{1,3}\.|192\.168\.[0-9]{1,3}\.)[0-9]{1,3}\b":
            "private/local IPv4 address",
    }
    text_suffixes = {".cff", ".json", ".log", ".md", ".ps1", ".py", ".tsv", ".txt", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "release" in path.parts:
            continue
        if path.suffix.lower() not in text_suffixes and path.name not in {"LICENSE", ".gitignore"}:
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        for expression, label in forbidden.items():
            require(re.search(expression, text, re.IGNORECASE) is None,
                    f"{label} found in {path.relative_to(ROOT)}")


def run_python_reproduction() -> None:
    script = DOSSIER / "independent_verification" / "python" / "verify.py"
    completed = subprocess.run(
        [sys.executable, str(script)],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    require("PYTHON_PROTH_VERDICT=PROVEN_PRIME" in completed.stdout,
            "Python reproduction did not return PROVEN_PRIME")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="repeat exact modular verification")
    arguments = parser.parse_args()
    validate_number()
    validate_metadata()
    validate_hashes()
    validate_links()
    validate_publication_safety()
    if arguments.full:
        run_python_reproduction()
    print(f"publication_validation=PASS full={str(arguments.full).lower()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"publication_validation=FAIL reason={error}", file=sys.stderr)
        raise SystemExit(1)
