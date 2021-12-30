import random
import functools
import os

# Letters in the alphabet (used to index the Markov matrix)
# \0 corresponds to the beginning or end of the word
letters = ['\0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Markov matrix for entries
# Each row corresponds to one previous letter
# Each column corresponds to one possible next letter, where the cells display the times each 2-letter combination occured in a name
# Note: I switched around the names "row" and "column" in all the code but I can't be bothered to fix it
matrix = []

# Names from the dataset
names = []
with open(os.path.dirname(os.path.abspath(__file__)) + '/names-1880.txt') as file:
	names = list(map(lambda x:x.lower(), file.read().splitlines()))

# Initialize the matrix, filling with zeroes
for l in letters:
	column = []
	for l2 in letters:
		column.append(0)
	matrix.append(column)

# Read all the names into the array
for name in names:
	# i counts the second letter in the pair
	for i in range(len(name)):
		# If this is the first letter, increase the probability for the letter to be chosen as the start letter
		# Otherwise, log the pair in the appropriate cell
		if(i == 0):
			matrix[0][letters.index(name[i])] += 1
		else:
			matrix[letters.index(name[i-1])][letters.index(name[i])] += 1
	# Set the last letter to be more likely to end the name
	matrix[letters.index(name[len(name)-1])][0] += 1

# Generate the names
def generate_name(min_len = 3, max_len = 20):
	# While we can't find a proper name
	while True:
		# Set some variables
		# The row to choose from
		column = matrix[0]
		# The previous letter generated
		letter = ''
		# The current name
		name = ''
		
		# While we haven't found a letter:
		while letter != '\0':
			# Find the total of the entries in the row
			total = functools.reduce(lambda x, y: x+y, column)
			x = random.randrange(0, total)
			
			# Choose the next letter weighted on the frequencies
			idx = 0
			for item in column:
				x -= item
				if(x <= 0):
					letter = letters[idx]
				else:
					idx += 1
			name += letter
			column = matrix[idx]

		# Try again if we generated too few or too many letters
		if len(name) < (min_len + 1) or len(name) > max_len:
			continue

		consonants = 0
		vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']	# count y

		too_many = False

		# Check if we have 4 consonants in a row; if so, try again
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

		# Convert to uppercase
		name = name[0].upper() + name[1:-1]

		return name
