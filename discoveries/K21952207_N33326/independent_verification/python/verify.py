import sys

sys.set_int_max_str_digits(20_000)

k = 21_952_207
n = 33_326
witness = 3
candidate = k * (1 << n) + 1
residue = pow(witness, (candidate - 1) // 2, candidate)

print(f"PYTHON_VERSION={sys.version.split()[0]}")
print(f"K={k}")
print(f"N_EXPONENT={n}")
print(f"DECIMAL_DIGITS={len(str(candidate))}")
print(f"K_LT_2_POW_N={int(k < (1 << n))}")
print(f"PROTH_WITNESS_BASE={witness}")
print(f"PROTH_CONGRUENCE={int(residue == candidate - 1)}")
print(
    "PYTHON_PROTH_VERDICT="
    + ("PROVEN_PRIME" if k < (1 << n) and residue == candidate - 1 else "NOT_PROVEN")
)
