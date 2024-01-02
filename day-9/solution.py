def processFile():
	input = []

	lines = open("input.txt", "r").read().split("\n")
	for line in lines:
		input.append(list(map(int, line.split())))

	return input

def predict(list):
	sequences = [list]

	lastSequence = sequences[-1]
	while any(lastSequence):
		newSequence = []
		for i in range(1, len(lastSequence)):
			newSequence.append(lastSequence[i] - lastSequence[i-1])
		lastSequence = newSequence
		sequences.append(lastSequence)

	sequences[-1].append(0)
	for j in range(len(sequences) - 2, -1, -1):
		nextSequence = sequences[j + 1]
		sequences[j].append(sequences[j][-1] + nextSequence[-1])

	return sequences[0][-1]

input = processFile()
result = 0
for list in input:
	result += predict(list)
print(result)