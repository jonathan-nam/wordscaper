import sys
from itertools import permutations

MIN_WORD_LEN = 3

if __name__ == "__main__":
	f = open('words_alpha.txt', 'r')
	
	chars = sys.argv[1]
	max_word_len = int(sys.argv[2])
	all_permutations = []
	possible_words = []
	
	for i in range(MIN_WORD_LEN, max_word_len+1):
		all_permutations += [''.join(p) for p in permutations(chars, i)]
	
	for line in f:
		word = line.strip()
		if word in all_permutations:
			possible_words.append(word)
			
	f.close()
	
	# Sort by length
	# And then by alphabetical order
	
	possible_words.sort()
	possible_words.sort(key=len)
	
	for word in possible_words:
		print(word)