import re
from functools import cmp_to_key

charValues = {
	'A': 14,
	'K': 13,
	'Q': 12,
	'J': 11,
	'T': 10,
	'9': 9,
	'8': 8,
	'7': 7,
	'6': 6,
	'5': 5,
	'4': 4,
	'3': 3,
	'2': 2
}

rankings = [
	[5],	# 0
	[4],	# 1
	[3, 2],	# 2
	[3],	# 3
	[2, 2],	# 4
	[2],	# 5
]

def processFile():
	hands = {}

	lines = open("input.txt", "r").read().split("\n")
	for line in lines:
		results = re.findall(r'[A-Za-z0-9]+', line)
		hands[results[0]] = results[1]

	return hands

def findTypes(hands):
	types = {}
	for hand in hands:
		types[hand] = findType(hand)
	return types

def findType(hand):
	charCount = {}
	for char in hand:
		if char in charCount:
			charCount[char] += 1
		else:
			charCount[char] = 1

	occurrences = list(filter(lambda a: a != 1, charCount.values()))
	for i in range(0, len(rankings)):
		if sorted(occurrences) == sorted(rankings[i]):
			return i
	return len(rankings)
	

def compareHands(hand1, hand2):
	global types
	type1 = types[hand1]
	type2 = types[hand2]

	if type1 == type2:
		for i in range(0, len(hand1)):
			value1 = charValues[hand1[i]]
			value2 = charValues[hand2[i]]
			if value1 != value2:
				return value2 - value1
		return 0
	else:
		return type1 - type2

bids = processFile()
types = findTypes(bids.keys())
sortedHands = sorted(bids.keys(), key=cmp_to_key(compareHands))

result = 0
for i in range(0, len(sortedHands)):
	sh = sortedHands[i]
	rank = len(sortedHands) - i
	print(sh, " has rank ", str(rank), " and type ", str(types[sh]))
	bid = int(bids[sh]) * rank
	result += bid

print(result)