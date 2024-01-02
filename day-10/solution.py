import math

diagram = []
start = []

def processFile():
	global diagram
	global start

	lines = open("input.txt", "r").read().split("\n")
	for i in range(0, len(lines)):
		line = lines[i]
		row = []
		for j in range(0, len(line)):
			char = line[j]
			if char == 'S':
				start = [i, j]
			row.append(char)
		diagram.append(row)

	return start, diagram

def findFirstNodes():
	result = []

	i = start[0]
	j = start[1]

	above = diagram[i-1][j] if i > 0 else None
	below = diagram[i+1][j] if i+1 < len(diagram) else None
	left = diagram[i][j-1] if j > 0 else None
	right = diagram[i][j+1] if j+1 < len(diagram[i]) else None

	if above == '7' or above == 'F' or above == '|':
		result.append([i-1, j])

	if below == 'L' or below == 'J' or below == '|':
		result.append([i+1, j])

	if left == '-' or left == 'L' or left == 'F':
		result.append([i, j-1])

	if right == '-' or right == 'J' or right == '7':
		result.append([i, j+1])

	return result

def getNeighbors(node):
	i = node[0]
	j = node[1]
	char = diagram[i][j]
	fields = []
	match char:
		case '|': 
			fields = [[i-1, j], [i+1, j]]
		case '-': 
			fields = [[i, j-1], [i, j+1]]
		case 'L':
			fields = [[i-1, j], [i, j+1]]
		case 'J':
			fields = [[i, j-1], [i-1, j]]
		case '7':
			fields = [[i, j-1], [i+1, j]]
		case 'F':
			fields = [[i, j+1], [i+1, j]]

	return fields #[f for f in fields if fieldExists(f)]

def isSameNode(node1, node2):
	result = node1[0] == node2[0] and node1[1] == node2[1]
	print("Is same node", node1, node2, result)
	return result

def traverse():
	prevNode = start
	nextNode, _ = findFirstNodes()
	count = 1

	i = nextNode[0]
	j = nextNode[1]

	while nextNode[0] != start[0] or nextNode[1] != start[1]:
		currentNode = nextNode
		neighbors = getNeighbors(currentNode)
		print("Previous node", prevNode)
		print("Current node", nextNode)
		print("Neighbors", neighbors)
		
		nextNode = neighbors[0] if isSameNode(prevNode, neighbors[1]) else neighbors[1]
		count += 1
		prevNode = currentNode
		print("Next node", nextNode)
		print("Count", count)
		print()

	return math.floor(count / 2)


processFile()
print(traverse())


# |
# -
# L
# J
# 7
# F
# .
# S

# up: i-1
# down: i+1
# left: j-1
# right: j+1

