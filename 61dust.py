#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185 as mcb

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Outputs sequence with low entrpy regions masked.')
# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='requires fasta file')
parser.add_argument('--windowsize', required=True, type=int,
	metavar='<int>', help='requires window size')
parser.add_argument('--entropy threshold', required=True, type=float,
	metavar='<float>', help='requires entropy threshold')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='lowercase or N-based masking. N-based default')
# finalization
arg = parser.parse_args()

output = ''
for name, seq in mcb.read_fasta(arg.fasta):
	for i in range(0, len(seq)-arg.windowsize+1):
		window = seq[i:i+arg.windowsize]
		if mcb.hcalc(window) < arg.threshhold:
			if arg.lowercase: output += window.lower()
			else:             output += 'n' * arg.windowsize
		else: output += window
print(name, output)
		
		
		
