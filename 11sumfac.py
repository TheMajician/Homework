#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here
s = 0
f = 1

for i in range(1, n+1):
	s += i
	f *= i
print(n, s, f)

#I worked on this with Inglis, Paul, and Jeremy

"""
python3 11sumfac.py
5 15 120
"""
