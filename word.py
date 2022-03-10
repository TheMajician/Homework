import sys
import argparse
import random

# WORD
# words of real langages


# read in text file
language = sys.argv[1]
lang =''
exclude = ".,?\"!:;[]_"
w1 = ''
w2 = {}
w3 = {}
for a in range(2):
	with open(language) as fp:
		for line in fp.readlines():
			words = line.split()
			for word in words:
				for ex in exclude:
					word = word.replace(ex,"")
				word += "$"
				w1 += word[0]
				for i in range(1, len(word)):
					prev = word[i-1]
					this = word[i]
					if prev not in w2: w2[prev] = ''
					w2[prev] += this
				for i in range(2, len(word)):
					prev = word[i-2:i]
					this = word[i]
					if prev not in w3: w3[prev] = ''
					w3[prev] += this
	language = sys.argv[2]
#print(w3)

for i in range(50):
	name = ''
	first = random.choice(w1)
	second = random.choice(w2[first])
	name += first + second
#	print(name)
	last = first + second
	if last not in w3: continue
	while True:		
		next = random.choice(w3[last])
		if next == "$": break
		name += next
#		print(name, next)
		last = name[-2:]
	print(name)







