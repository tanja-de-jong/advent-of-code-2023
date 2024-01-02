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
			seeds = list(map(int, line.split()[1:]))
		elif line.endswith("map:"):
			index = index + 1
			mappings.append([])
		else:
			numbers = line.split()
			mappings[index].append({
				"dest_start": numbers[0],
				"source_start": numbers[1],
				"range": numbers[2]	
			})

def getMappedValue(input, mapping):
	# Map an input value to an output value using a given mapping
	for m in mapping:
		destStart = int(m["dest_start"])
		sourceStart = int(m["source_start"])
		length = int(m["range"])

		if sourceStart <= input < (sourceStart + length):
			diff = input - sourceStart
			return destStart + diff

	return input

processData()
result = None
for seed in seeds:
	output = [seed]
	for i in range(0, len(mappings)):
		output.append(getMappedValue(output[-1], mappings[i]))

	lastValue = output[-1]
	if result is None or lastValue < result:
		result = lastValue

print(result)