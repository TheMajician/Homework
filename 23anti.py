#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA' [::-1]
rc = ''
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'A': rc += 'T'
	elif nt == 'T': rc += 'A'
	elif nt == 'G': rc += 'C'
	else: rc += 'G'
	
print(rc)

#worked with Inglis, Kim, Iris

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
