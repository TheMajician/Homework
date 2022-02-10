#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

#print(sys.argv)

# make imput into floats and a list
nums= []
for i in range(1, len(sys.argv)): 
	nums.append(float(sys.argv[i]))
	
count = len(nums)
#print(nums)
print('Count:', count)

# minimum and maximum
nums.sort()
min = nums[0]
l = len(nums)
max = nums[l-1]
print('Minimum:', min)
print('Maximum:', max)

# mean
sum = sum(nums)
mean = sum/count
print(f'Mean: {mean:.3f}')

# std
sumvari = 0
for i in range(len(nums)):
	vari = (nums[i] - mean)**2
	sumvari += vari
avg = sumvari/l
std = avg**0.5
print(f'Std. dev: {std:.3f}')

# Median
if len(nums)%2 ==0:
	mid = int(len(nums)/2)  #average it out
	median = (nums[mid-1]+nums[mid])/2
else:
	mid = int((len(nums)+1)/2)
	median = nums[mid-1]
print("Median:", median)
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
