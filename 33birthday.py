#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

ppl = 23
trl = 5000
shared = 0

for t in range(trl):
	cal = [0]*365
	for p in range(ppl):
		r = random.randint(0, len(cal)-1)
		cal[r] += 1
		#print(cal)
	for value in cal:
		if value > 1: 
			shared += 1
			break
print("Chance to share a birthday:", shared/trl)

"""
# Practice	
shared = 0
L = [0, 0, 0, 1, 2, 1, 0, 1, 2]
for value in L:
	if value > 1: 
		shared += 1   # not working, always give shared = 0	
		break
print(shared)
"""

"""
python3 33birthday.py
0.571
"""

