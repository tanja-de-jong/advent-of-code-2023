words = open("input.txt").read().split()

result = 0

def getFirst(word):
	return getFirstDigit(word, 0, len(word), 1)		

def getLast(word):
	return getFirstDigit(word, len(word) - 1, -1, -1);

def getFirstDigit(word, start, end, step):
	for i in range(start, end, step):
		char = word[i]
		if char.isdigit():
			return char

for word in words:
	first = getFirst(word)
	last = getLast(word)
	result += int(first + last)
	print("Sum", result)