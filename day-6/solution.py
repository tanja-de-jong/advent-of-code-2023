import re
import math

times = []
records = []

def processFile():
	global times
	global records

	lines = open("test-input.txt", "r").read().split("\n")
	times =  list(map(int, re.findall(r'(\d+)', lines[0])))
	records =  list(map(int, re.findall(r'(\d+)', lines[1])))

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

processFile()

result = 1
for i in range(0, len(times)):
# 	result = result * trySolutions(times[i], records[i]) # Brute force solution
	result = result * computeSolution(times[i], records[i]) # Mathematical solution
print(result)