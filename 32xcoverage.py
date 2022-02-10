#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

if len(sys.argv) != 4:
	print("Please Imput: genome size, read number, read length")
	sys.exit()
	
gsize = int(sys.argv[1])
rnum = int(sys.argv[2])
rlen = int(sys.argv[3])
genome = []

for i in range(gsize):
	genome.append(0)
#print(genome)

for j in range(rnum):
	r = random.randint(0, gsize-rlen)	
	for i in range(r, r+rlen):
		genome[i] += 1
#print(genome)
# Minimum and Maximum
genome.sort()
min = genome[0]
max = genome[gsize-1]
# Average
sum = 0
for x in genome[rlen: -rlen]:
	sum += x
avg = sum/(gsize-2*rlen)

print(f'{min} {max} {avg:.3f}')

# random???
# r = 17


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
