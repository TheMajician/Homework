#!/usr/bin/env python3

import random

# 06 Ring or Cloak?

rolls = 100

#Fire Ring
ring = 0
cloak = 0
print(f'DC Value RingSaves CloakSaves')
for DC in range(1, 21):
	for i in range(rolls):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1+5 > DC: ring += 1
		if r1 > r2 and r1 >= DC: cloak += 1
		if r2 > r1 and r2 >= DC: cloak += 1
	print(f'\t{DC}\t{ring/rolls:.1f}\t{cloak/rolls:.1f}')
print("Fire Ring has slight advantage over Fire Cloak")
