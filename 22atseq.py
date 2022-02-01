#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

#print(random)
size = 30
dna = ''
AT = 0
for i in range(size):
	r = random.random()
	if   r < 0.3:
		dna += 'A'
		AT += 1
	elif r < 0.6: 
		dna += 'T'
		AT += 1
	elif r < 0.8: 
		dna += 'G'
	else:         
		dna += 'C'

print(f'{size}, {AT/size:.2f}, {dna}')

# did in class

#=============================================================
#alternative method from class using random.choice
"""
GC = 0
gcseq ="AAATTTCCGG" #number of nt in string give percentage
newseq =""
for i in range(30):
	nt = random.choice(gcseq)
	newseq += nt
	if nt == 'C' or nt == 'G': GC +=1
print(f'{len(newseq)}, {GC/len(newseq):.3f}, {newseq}')

"""
"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
