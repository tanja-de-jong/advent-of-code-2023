import re

gear = '*'
lines = open("input.txt").read().split()

width = len(lines[0])
height = len(lines)

def getCoordinates():
	numbers = []
	coordinates = []
	current_co = []
	current_num = ""
	gears = []
	gearAdjacents = []
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
				if char == gear:
					gears.append(str(x) + "," + str(y))
					gearAdjacents.append(getAdjacentFields(char, x, y))
	return gears, gearAdjacents, numbers, coordinates

def getAdjacentFields(char, xSymbol, ySymbol):
	result = []
	for x in range(max(0, xSymbol-1), min(width, xSymbol+2)):
		for y in range(max(0, ySymbol-1), min(height, ySymbol+2)):
			if x != xSymbol or y != ySymbol:
				result.append(str(x) + "," + str(y))
	return result

def findMatches(gears, gearAdjacents, numbers, coordinates):
	sum = 0
	for i in range(0, len(gears)):
		gearFields = gearAdjacents[i]
		# for every gear
		gearNumbers = []
		for j in range(0, len(numbers)):
			# for every number
			# check if number is adjacent to gear
			# numberfields match any of gearadjacents
			numberFields = coordinates[j]
			intersection = set(gearFields).intersection(set(numberFields))
			if intersection:
				gearNumbers.append(numbers[j])

		if len(gearNumbers) == 2:
			gearRatio = int(gearNumbers[0]) * int(gearNumbers[1])
			sum += gearRatio
	print(sum)

gears, gearAdjacents, numbers, coordinates = getCoordinates()
findMatches(gears, gearAdjacents, numbers, coordinates)
