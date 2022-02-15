#!/usr/bin/env python3
import random
# 03 halfling's luck


trl = 10000
rev = 0
die = 0
sta = 0

for i in range(trl):
	fail = 0
	suc = 0
	while True:
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 == 1: 
			if r2 == 1:    fail += 2
			elif r2 < 10:  fail += 1
			elif r2 == 20: 
				rev += 1
				break
			else:          suc += 1
		
		elif r1 < 10:  fail += 1
		elif r1 == 20: 
			rev +=1
			break
		else:          suc += 1
	
		if fail == 3: 
			die += 1
			break
		if suc == 3: 
			sta += 1
			break
		
print("Hafling's chances to...")
print(F'Die: {die/trl}')
print(f'Stabilize: {sta/trl}')
print(f'Revive: {rev/trl}')
	
