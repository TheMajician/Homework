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
"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
