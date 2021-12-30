import random
import functools
import os

letters = ['\0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

matrix = []

names = []
with open(os.path.dirname(os.path.abspath(__file__)) + '/names-1880.txt') as file:
	names = list(map(lambda x:x.lower(), file.read().splitlines()))

for l in letters:
	column = []
	for l2 in letters:
		column.append(0)
	matrix.append(column)

for name in names:
	for i in range(len(name)):
		if(i == 0):
			matrix[0][letters.index(name[i])] += 1
		else:
			matrix[letters.index(name[i-1])][letters.index(name[i])] += 1
	matrix[letters.index(name[len(name)-1])][0] += 1

def generate_name(min_len = 3, max_len = 20):
	while True:
		column = matrix[0]
		letter = ''
		name = ''
		accepted = True
		while letter != '\0':
			total = functools.reduce(lambda x, y: x+y, column)
			x = random.randrange(0, total)
			idx = 0
			for item in column:
				x -= item
				if(x <= 0):
					letter = letters[idx]
				else:
					idx += 1
			name += letter
			column = matrix[idx]

		if len(name) < (min_len + 1) or len(name) > max_len:
			continue

		consonants = 0
		vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']	# count y

		too_many = False

		for letter in name:
			if letter in vowel_list:
				consonants = 0
			else:
				consonants += 1
				if consonants > 3:
					too_many = True
					break

		if too_many:
			continue

		name = name[0].upper() + name[1:-1]

		return name
