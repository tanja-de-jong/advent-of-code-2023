import re

def processFile():
	instructions = ""
	moves = {}

	lines = open("input.txt", "r").read().split("\n")
	instructions = lines[0]
	for i in range(2, len(lines)):
		nodes = re.findall(r'[A-Z]+', lines[i])
		moves[nodes[0]] = {
			"L": nodes[1],
			"R": nodes[2]
		}
	return instructions, moves

def move(moves, instructions):
	node = "AAA"
	count = 0
	while node != "ZZZ":
		step = instructions[count % len(instructions)]
		node = moves[node][step]
		count += 1

	return count

instructions, moves = processFile()
count = move(moves, instructions)
print(count)
