#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys


nums =[]
sum = 0
tolerance = 0.01
ent = 0

for i in range(1, len(sys.argv)):
	nums.append(float(sys.argv[i]))
	sum += float(sys.argv[i])

if abs(sum -1.0) > tolerance:
	print("Probablilities do not sum to 1.00")
	sys.exit()
	
for prb in nums:
	ent += -(prb*math.log2(prb))
print(f'Entropy: {ent:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
