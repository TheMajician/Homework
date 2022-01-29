#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
count = 0
for i in range(len(dna)):
	if dna[i] == 'G' and 'C':   count += 1
	elif dna[i] == 'C': count += 1
frac= count/len(dna)

#Method 1 - old school print style
print('%.2f' % (frac))
#Method 2 - str. format
print('{:.2f}' .format(frac))
#Method 3 - f strings
print(f'{count/len(dna):.2f}')

#did in class

"""
python3 21gc.py
0.42
0.42
0.42
"""
