import re
import re

file = open("input.txt", "r")
lines = file.readlines()

cards = [1] * len(lines)
for i in range(0, len(lines)):
	line = lines[i]
	parts = line.split(":")[1].split("|")
	winning_numbers = re.findall(r'\d+', parts[0])
	actual_numbers = re.findall(r'\d+', parts[1])

	overlap = len(set(winning_numbers).intersection(actual_numbers))

	for j in range(i+1, i+1+overlap):
		cards[j] = cards[j] + cards[i]

print(sum(cards))