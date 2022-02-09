#!/usr/bin/env python3
import random

rolls = 20
fail = 0
suc = 0
die = 0
sta = 0
rev = 0

print(f'Number of Rolls\tDeath\tStablize\tRevive')
for i in range(1, rolls+1):
	r = random.randint(1, 20)
	if   r == 1 : fail += 2
	elif r < 10: fail += 1
	elif r == 20 : rev +=1
	elif r >= 10 : suc += 1
	
	if fail == 3: die += 1
	if suc == 3: sta += 1
	print(f'{i}\t{die/rolls}\t{sta/rolls}\t{rev/rolls}') 

#not giving correct probabilities...
	
	
		
