#!/usr/bin/env python3
import random

trl = 10000
die = 0
sta = 0
rev = 0

for i in range(trl):
	fail = 0
	suc = 0
	while True:
		r = random.randint(1, 20)
	
		if   r == 1 : fail += 2
		elif r < 10 : fail += 1
		elif r ==20: 
			rev += 1
			break
		else:        suc += 1
		if fail >= 3:
			die += 1
			break
		if suc >= 3:
			sta += 1
			break
			
print("Chances to...")
print(F'Die: {die/trl}')
print(f'Stabilize: {sta/trl}')
print(f'Revive: {rev/trl}')

	
		
