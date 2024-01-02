import re

file = open("test-input.txt", "r")
sum = 0
for line in file:
	parts = line.split(":")[1].split("|")
	winning_numbers = re.findall(r'\d+', parts[0])
	actual_numbers = re.findall(r'\d+', parts[1])
	overlap = len(set(winning_numbers).intersection(actual_numbers))
	score = 0
	if overlap:
		score = pow(2, overlap - 1)
	sum += score

print(sum)

