from random import random

for a in range(150):
	sentence = ""
	for b in range(51):
		rand = random()
		if rand < 0.5:
			sentence = sentence + " -1"
		else:
			sentence = sentence + " 1"
	print(sentence)