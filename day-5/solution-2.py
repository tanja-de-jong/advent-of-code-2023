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
				"source": range(sourceStart, sourceStart + length),
				"diff": destStart - sourceStart
			})

def applyMapping(mapping, index, input):
	result = []

	sourceMap = mapping[index]["source"]
	diff = mapping[index]["diff"]

	# find the first input range
	matchStart = max(input[0], sourceMap[0])
	matchEnd = min(input[-1], sourceMap[-1])
	
	noChange = range(input[0], min(input[-1] + 1, matchStart))
	if noChange:
		result.append(noChange)

	mappedRange = range(matchStart + diff, matchEnd + diff + 1)
	if mappedRange:
		result.append(mappedRange)

	if input[-1] > sourceMap[-1]:
		remainder = range(max(input[0], matchEnd + 1), input[-1] + 1)
		if remainder:
			if index < len(mapping) - 1:
				result += applyMapping(mapping, index + 1, remainder)
			else:
				result.append(remainder)
	return result


def getMappedRanges(inputList, mappings, index):
	if index >= len(mappings) - 1:
		return inputList

	# Map an input range to one or more output ranges using a given mapping
	orderedMapping = sorted(mappings[index], key=lambda m: m['source'][0])

	mappedList = []

	for input in inputList:
		mappedList += applyMapping(orderedMapping, 0, input)

	return getMappedRanges(mappedList, mappings, index + 1)

def getLowestLocationNumber(locationRanges):
	locationStartList = map(lambda lr: lr[0], locationRanges)
	return min(locationStartList)
		
processData()
endRanges = getMappedRanges(seeds, mappings, 0)
print(getLowestLocationNumber(endRanges))