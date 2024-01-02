import re
import math

def processFile():
	lines = open("input.txt", "r").read().split("\n")
	time =  int(''.join(re.findall(r'(\d+)', lines[0])))
	record =  int(''.join(re.findall(r'(\d+)', lines[1])))
	return time, record

def trySolutions(time, record):
	options = []
	for speed in range(0, time):
		distance = (time - speed) * speed
		if distance > record:
			options.append(speed)
	return len(options)

def computeSolution(time, record):
	b = time
	c = -record
	part1 = b * b
	part2 = 4 * -1 * c
	withinRoot = part1 - part2
	determinant = math.sqrt((b*b) - 4 * -1 * c)
	startTop = -b + determinant
	endTop = -b - determinant
	start = startTop / -2
	if start.is_integer():
		start = int(start + 1)
	else:
		start = math.ceil(start)

	end = endTop / -2
	if end.is_integer():
		end = int(end - 1)
	else:
		end = math.floor(end)

	return len(range(start, end + 1))

time, record = processFile()
# result = trySolutions(time, record)
result = computeSolution(time, record)

print(result)
