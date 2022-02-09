#!/usr/bin/env python3
import random

# 05 piercer

rolls = 10000

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
 		
#most optimal?
dam = 0
re = 6
for i in range(rolls):
	r1 = random.randint(1, 10)
	r2 = random.randint(1, 10)
	if r1 < re: dam += r2
	else:      dam += r1
print(f'Highest Average Damage: {dam/rolls} with re-rolls at {re-1}')
