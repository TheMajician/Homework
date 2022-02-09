#!/usr/bin/env python3
import random
# 03 halfling's luck

rolls = 20
fail = 0
suc = 0
rev = 0
die = 0
sta = 0

for i in range(1, rolls):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 == 1: 
		if r2 == 1:    fail += 2
		elif r2 < 10:  fail += 1
		elif r2 == 20: rev += 1
		else:          suc += 1
	elif r1 < 10:  fail += 1
	elif r1 == 20: rev +=1
	else:          suc += 1
	
	if fail == 3: die += 1
	if suc == 3: sta += 1
	print(f'{rolls}\t{die/rolls}\t{sta/rolls}\t{rev/rolls}')
	
	
