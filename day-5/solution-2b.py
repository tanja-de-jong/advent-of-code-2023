import time
seeds = []
mappings = []

def processData():
	global seeds
	global mappings

	# Process data into usable format
	lines = list(filter(None, open("input.txt", "r").read().split("\n")))
	index = -1
	for line in lines:
		if line.startswith("seeds:"):
			numbers = list(map(int, line.split()[1:]))
			for i in range(0, len(numbers) // 2):
				seedStart = numbers[i * 2]
				seedRange = numbers[i * 2 + 1]
				seeds.append(range(seedStart, seedStart + seedRange))
		elif line.endswith("map:"):
			index = index + 1
			mappings.append([])
		else:
			numbers = line.split()
			destStart = int(numbers[0])
			sourceStart = int(numbers[1])
			length = int(numbers[2])
			mappings[index].append({
				"dest": range(destStart, destStart + length),
				"diff": sourceStart - destStart
			})

def getMappedValue(input, mapping):
	# Map an input value to an output value using a given mapping
	for m in mapping:
		if input in m["dest"]:
			return input + m["diff"]
	return input

def tryLocations():
	location = 0
	found = False
	while not found:
		output = [location]
		for i in range(len(mappings) - 1, -1, -1):
			output.append(getMappedValue(output[-1], mappings[i]))
		seed = output[-1]
		for seedRange in seeds:
			if seed in seedRange:
				print(seed)
				print(location)
				found = True
				break;
		location = location + 1	

start = time.time()

processData()
tryLocations()

end = time.time()
print(end - start)