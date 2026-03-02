#!/usr/bin/env python

# nucPct.py
# Given a DNA or RNA sequence, compute the percentage of each nucleotide.

import re
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description="Compute nucleotide percentages for a DNA or RNA sequence")
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence (DNA or RNA)")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
seq = args.seq.upper()

# Validate allowed characters
if not re.fullmatch(r"[ACGTU]+", seq):
    print("Error: invalid characters (allowed: A C G T U)")
    sys.exit(1)

# Reject mixed T and U
if ("T" in seq) and ("U" in seq):
    print("Error: sequence contains both T and U (cannot be DNA nor RNA)")
    sys.exit(1)

total = len(seq)
counts = {base: seq.count(base) for base in "ACGTU"}

print(f"Length: {total}")
for base in "ACGTU":
    pct = (counts[base] / total) * 100
    print(f"{base}: {counts[base]} ({pct:.2f}%)")
