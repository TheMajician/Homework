#!/usr/bin/env python3

import random

# 04 Element Adept

trails = 1000

norm = 0
adep = 0

for i in range(trails):
	r = random.randint(1, 10)
	norm += r
	if r == 1: r = 2
	adep += r
	
normavg = norm/trails
adepavg = adep/trails
diff = adepavg - normavg
print(f'Normal\tAdept\tDifference')	
print(f'{normavg}\t{adepavg}\t{diff:.4f}')

