### Part one and two ###
s1, s2 = 0, 0
def unique_set(x):
	return len(x) == len(set(x))
with open('04.in','r') as f:
	for line in f:
		words = line.rstrip().split(' ')
		if len(words) == len(set(words)):
			s1 += 1
		wordsort = ["".join(sorted(word)) for word in words]
		if len(wordsort) == len(set(wordsort)):
			s2 += 1
print(s1,s2)
