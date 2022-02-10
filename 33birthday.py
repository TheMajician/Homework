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

cal = [0]*365
ppl = 25
trl = 5
for t in range(trl):
	shared = 0
	for p in range(ppl):
		r = random.randint(1, len(cal)-1)
		cal[r] += 1
		print(cal)
	for i in cal:
		if cal[i] > 1: shared += 1   # not working, always give shared = 0
	print(t, shared)

"""
python3 33birthday.py
0.571
"""

