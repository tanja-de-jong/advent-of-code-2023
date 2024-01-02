import re

def processData(input):
	groups = []
	file = open(input, "r")
	for line in file:
		red = re.findall(r'(\d+) red', line)
		green = re.findall(r'(\d+) green', line)
		blue = re.findall(r'(\d+) blue', line)
		groups.append({
			"red": red,
			"green": green,
			"blue": blue	
		})
	return groups

def isPossible(groups, redMax, greenMax, blueMax):
	sum = 0
	for i in range(0, len(groups)):
		group = groups[i]

		red = group["red"]
		redPossible = all(int(r) <= redMax for r in red)

		green = group["green"]
		greenPossible = all(int(g) <= greenMax for g in green)

		blue = group["blue"]
		bluePossible = all(int(b) <= blueMax for b in blue)

		if redPossible and greenPossible and bluePossible:
			sum += i + 1

	print(sum)

groups = processData("input.txt")
print(groups)
isPossible(groups, 12, 13, 14)