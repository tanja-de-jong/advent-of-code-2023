import re

symbols = {'!', '@', '#', '$', '%', '^', '&', '*'}
lines = open("input.txt").read().split()

width = len(lines[0])
height = len(lines)

# find symbols
for line in lines:
	res = re.findall(r'[^\d\.]+', line)
	symbols.update(res)

def getCoordinates():
	numbers = []
	coordinates = []
	current_co = []
	current_num = ""
	adjacent = []
	for y in range(0, len(lines)):
		for x in range(0, len(lines[y])):
			char = lines[y][x]
			if char.isdigit():
				current_num += char
				current_co.append(str(x) + "," + str(y))
			else:
				if current_num:
					numbers.append(current_num)
					coordinates.append(current_co)
					current_num = ""
					current_co = []
				if char in symbols:
					adjacent += getAdjacentFields(x, y)
	return adjacent, numbers, coordinates

def getAdjacentFields(xSymbol, ySymbol):
	result = []
	for x in range(max(0, xSymbol-1), min(width, xSymbol+2)):
		for y in range(max(0, ySymbol-1), min(height, ySymbol+2)):
			if x != xSymbol or y != ySymbol:
				result.append(str(x) + "," + str(y))
	return result

def findMatches(adjacent, numbers, coordinates):
	sum = 0
	for i in range(0, len(coordinates)):
		numberSet = coordinates[i]
		isAdjacent = any((True for x in numberSet if x in adjacent))
		if isAdjacent:
			sum += int(numbers[i])
	print(sum)

adjacent, numbers, coordinates = getCoordinates()
findMatches(adjacent, numbers, coordinates)
