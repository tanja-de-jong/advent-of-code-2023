from collections import deque

rows = 0
cols = 0

def processFile():
    global rows
    global cols

    galaxies = []
    
    lines = open("test-input.txt", "r").read().split("\n")
    
    rowsWithGalaxies = set(range(len(lines)))
    colsWithGalaxies = set(range(len(lines[0])))

    for i in range(0, len(lines)):
        line = lines[i]
        row = []
        for j in range(0, len(line)):
            char = line[j]
            if char == '#':
                galaxies.append([i, j])
                rowsWithGalaxies.discard(i)
                colsWithGalaxies.discard(j)
                
    for galaxy in galaxies:
        for row in rowsWithGalaxies:
            if galaxy[0] > row:
                galaxy[0] += 1
        for col in colsWithGalaxies:
            if galaxy[1] > col:
                galaxy[1] += 1

    rows = len(lines) - len(rowsWithGalaxies)
    cols = len(lines[0]) - len(colsWithGalaxies)

    return galaxies

def isValidField(field):
    i = field[0]
    j = field[1]
    return i > 0 and i+1 < rows-1 and j > 0 and j+1 < cols-1



def findDistances(galaxies):
    distances = {}
    for i in range(len(galaxies)):
        distances[i] = {}
        for j in range(len(galaxies)):
            if i == j:
                distances[i][j] = 0
            else:
                distances[i][j] = float('inf')

    for i in range(len(galaxies)):
        visited = set()
        queue = deque([(galaxies[i], 0)])
        while queue:
            current, distance = queue.popleft()
            print(current)
            print(visited)
            if current not in visited:
                visited.add(current)
                if isValidField(current):
                    row, col = current
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                new_row = row + dx
                                new_col = col + dy
                                neighbor = (new_row, new_col)
                                if neighbor in galaxies:
                                    neighbor_index = galaxies.index(neighbor)
                                    distances[i][neighbor_index] = distance + 1
                                    queue.append((neighbor, distance + 1))

    return distances

galaxies = processFile()
distances = findDistances(galaxies)
print(distances)
