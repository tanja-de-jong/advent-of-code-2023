import re
import math

def processFile():
	instructions = ""
	moves = {}
	start_nodes = set()

	lines = open("input.txt", "r").read().split("\n")
	instructions = lines[0]
	for i in range(2, len(lines)):
		nodes = re.findall(r'[A-Z1-9]+', lines[i])
		origin_node = nodes[0]
		moves[origin_node] = {
			"L": nodes[1],
			"R": nodes[2]
		}
		if origin_node[-1] == 'A':
			start_nodes.add(origin_node)
	return start_nodes, instructions, moves


def move(node, moves, instructions):
	count = 0
	while node[-1] != 'Z':
		step = instructions[count % len(instructions)]
		node = moves[node][step]
		count += 1

	return count

start_nodes, instructions, moves = processFile()
lcm = 1
for node in start_nodes:
	count = move(node, moves, instructions)
	print(count)
	lcm = lcm * count // math.gcd(lcm, count)
	a = [100, 200, 150]   #will work for an int array of any length

print(lcm)

# def move(nodes, moves, instructions):
# 	count = 0
# 	while any(node[-1] != 'Z' for node in nodes):
# 		print(nodes)
# 		for i in range(0, len(nodes)):
# 			step = instructions[count % len(instructions)]
# 			nodes[i] = moves[nodes[i]][step]
# 		count += 1
# 	return count