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

#===========================================
#class notes
	#range(len(dna)-1, -1, -1)
	# or use backwards = len(dna)-1-1
	# for nt in dna[::-1] print(nt):   if else etc
	
rev =''
for i in range(len(dna)-1, -1, -1): #still not backwards....
	nt = dna[i]
	if   nt == 'A': rev += 'T'
	elif nt == 'T': rev += 'A'
	elif nt == 'C': rev += 'G'
	else:           rev += 'C'
print(rev)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
