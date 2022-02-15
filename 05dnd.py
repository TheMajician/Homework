#!/usr/bin/env python3
import random

# 05 piercer

rolls = 10000

#most optimal?
re = 6
for re in range(1, 8):
	dam = 0
	for i in range(rolls):
		r1 = random.randint(1, 10)
		r2 = random.randint(1, 10)
		if r1 < re: dam += r2
		else:      dam += r1git 
	print(f'Re-roll {re} Average Damage: {dam/rolls}')
	
	
	
# Old code for each re-roll value
"""
#Jorg
jdam = 0
for i in range(rolls):
 	r1 = random.randint(1, 10)
 	r2 = random.randint(1, 10)
 	if r1 < 7: jdam += r2
 	else:      jdam += r1
print(f'Jorg:{jdam/rolls}')
 
#Gastin
gdam = 0
for i in range(rolls):
	r1 = random.randint(1, 10)
	r2 = random.randint(1, 10)
	if r1 < 4: gdam += r2
	else:      gdam += r1
print(f'Gastin:{gdam/rolls}')
"""
