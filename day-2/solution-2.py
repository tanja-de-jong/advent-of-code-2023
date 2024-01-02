import re

def processData(input):
	groups = []
	file = open(input, "r")
	for line in file:
		red = re.findall(r'(\d+) red', line)
		green = re.findall(r'(\d+) green', line)
		blue = re.findall(r'(\d+) blue', line)
		groups.append({
			"red": list(map(int, red)),
			"green": list(map(int, green)),
			"blue": list(map(int, blue))
		})
	return groups

def getPower(groups):
	sum = 0
	for group in groups:
		red = max(group["red"])
		green = max(group["green"])	
		blue = max(group["blue"])
		power = red * green * blue
		sum += power

	print(sum)

groups = processData("input.txt")
getPower(groups)