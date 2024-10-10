# O(wh) time | O(wh) space
def riverSizes(matrix):
	visited = [[False for col in row] for row in matrix]
	sizes = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if visited[i][j]:
				continue
			traverseNodes(i, j, matrix, visited, sizes)
	return sizes

def traverseNodes(i, j, matrix, visited, sizes):
	nodesToExplore = [[i, j]]
	currentRiverSize = 0
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbors = getUnvisitedNeighbors(i, j, visited, matrix)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)
		
def getUnvisitedNeighbors(i, j, visited, matrix):
	unvisitedNeighbors = []
	if i != 0 and not visited[i - 1][j]:
		unvisitedNeighbors.append([i - 1, j])
	if i != len(matrix) - 1 and not visited[i + 1][j]:
		unvisitedNeighbors.append([i + 1, j])
	if j != len(matrix[0]) - 1 and not visited[i][j + 1]:
		unvisitedNeighbors.append([i, j + 1])
	if j != 0 and not visited[i][j - 1]:
		unvisitedNeighbors.append([i, j - 1])
	return unvisitedNeighbors
	


matrix = [
	[1, 0, 0, 1, 0],
	[1, 0, 1, 0, 0],
	[0, 0, 1, 0, 1],
	[1, 0, 1, 0, 1],
	[1, 0, 1, 1, 0]
]

print(riverSizes(matrix))
