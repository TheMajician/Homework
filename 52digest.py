#!/usr/bin/env python3
# 52digest.py

import re
import sys


# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


filename = sys.argv[1]
rp = str(sys.argv[2]).upper()
with open(filename) as fp:
	name = None
	after_origin = False
	seq = ''
	for line in fp.readlines():
		if line.startswith('ACESSION'):
			words = line.split()
			name = words[1]
		elif line.startswith("ORIGIN"):
			after_origin = True
		else:
			if after_origin:
				words = line.split()
				seq += ''.join(words[1:]).upper()
	#print(name, seq)
locs = []
for match in re.finditer(rp, seq):
	locs.append(match.start())
#print(locs)

#offset = sys.argv[3]
start = 0
end = len(seq)
for loc in locs:
	frag = loc - start
	start = loc # + offset      
#add if cutsite is not at begining of site (offset here = +1)
	print(frag)
print(end - locs[-1])


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
