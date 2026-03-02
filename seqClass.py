#!/usr/bin/env python

# seqClass.py
# Classify an input sequence as DNA/RNA (or neither) and optionally search for a motif.

import sys
import re
from argparse import ArgumentParser

# Set up command-line arguments
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif (optional)")

# If no arguments were provided, show help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Normalize input to uppercase so lowercase input works
args.seq = args.seq.upper()

# Validate and classify the sequence
if re.fullmatch(r'[ACGTU]+', args.seq):
    has_t = 'T' in args.seq
    has_u = 'U' in args.seq

    # Reject sequences containing both T and U (cannot be DNA nor RNA)
    if has_t and has_u:
        print('The sequence is not DNA nor RNA')
    elif has_t:
        print('The sequence is DNA')
    elif has_u:
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

# Optional motif search
if args.motif:
    args.motif = args.motif.upper()
    print(
        f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ',
        end=''
    )
    if re.search(args.motif, args.seq):
        print("FOUND - MOTIF VERSION")
    else:
        print("NOT FOUND (motif)")

