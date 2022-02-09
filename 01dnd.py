#!/user/bin/env python3

import random

# 1: Saving Throw

trials = 1000


print("DC Value", end ='\t')
print("Normal", end ='\t')
print("Adv", end ='\t')
print("Dis")
#for i in range(trials):
for DC in range(1, 21):
	normal = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		# Normal
		if r1 >= DC: normal += 1
		else:       normal += 0  
		# Advantage	
		if r1 > r2 and r1 >= DC: adv += 1
		if r2 > r1 and r2 >= DC: adv += 1
		# Disadvantage
		if r1 < r2 and r1 >= DC: dis +=1
		if r2 < r1 and r2 >= DC: dis +=1

	print(f'\t{DC}\t{normal/trials}\t{adv/trials}\t{dis/trials}')

