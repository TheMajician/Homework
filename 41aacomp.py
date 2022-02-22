#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# 
# Sorting the amino acids by frequency is optional

filename = sys.argv[1]
def readfasta(filename):
	records = []
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue
			if line[0] == ">":
				#ids.append(words[0][1:])
				if seq != '': 
					records.append((id, seq))
				words = line.split()
				id = words[0][1:]
				seq = ''
			else: 
				seq += line
		records.append((id, seq))
	return records

aas = "ACDEFGHIKLMNPQRSTVWY"

amount = [0]* len(aas)
total = 0
for id, seq in readfasta(filename):
	total += len(seq)-1
	for i in range(len(aas)):
		amount[i] += seq.count(aas[i])
for i in range(len(aas)):
	print(aas[i], amount[i], amount[i]/total)
	
	
"""
# Dont do
for aa in aas:	
	count = 0
	for id, seq in readfasta(filename):
		count += seq.count(aa)
	print(aa, count)
"""			

"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

