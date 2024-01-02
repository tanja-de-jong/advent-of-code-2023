words = open("input.txt").read().split()

result = 0

def getFirst(word):
	return getFirstDigit(word, 0, len(word), 1)		

def getLast(word):
	return getFirstDigit(word, len(word) - 1, -1, -1);

def getFirstDigit(word, start, end, step):
	substring = ""
	for i in range(start, end, step):
		char = word[i]
		if step > 0:
			substring = substring + char
		else:
			substring = char + substring
			
		if char.isdigit():
			return char
		else:
			digit = findDigit(substring)
			if digit:
				return digit

def findDigit(word):
	text_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

	for key in text_digits.keys():
		new_word = word.replace(key, text_digits[key])
		if new_word[0].isdigit():
			return new_word[0]
		elif new_word[-1].isdigit():
			return new_word[-1]


for word in words:
	first = getFirst(word)
	last = getLast(word)
	result += int(first + last)
	print("Sum", result)

