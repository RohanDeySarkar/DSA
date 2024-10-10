# Go to borders
# Check for connected ones
# Connected ones and 0's are TRUE
# Islands are FALSE
# Replace islands by 0

# O(wh) time | O(wh) space
def removeIslands(matrix):
	onesConnectedToBorder = [[False for col in row] for row in matrix]

	startRow = 0
	leftCol = 0
	endRow = len(matrix) - 1 
	rightCol = len(matrix[0]) - 1
	
	# check connectedOnes on 4 borders
	for row in range(len(matrix)):
		findConnectedOnes(matrix, row, leftCol, onesConnectedToBorder)
		findConnectedOnes(matrix, row, rightCol, onesConnectedToBorder)
		
	for col in range(len(matrix[0])):
		findConnectedOnes(matrix, startRow, col, onesConnectedToBorder)
		findConnectedOnes(matrix, endRow, col, onesConnectedToBorder)
			
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if onesConnectedToBorder[row][col] == False and matrix[row][col] == 1:
				matrix[row][col] = 0
	
	return matrix
			
def findConnectedOnes(matrix, row, col, onesConnectedToBorder):
	stack = [[row, col]]
	while len(stack):
		currentNode = stack.pop(0)
		row = currentNode[0]
		col = currentNode[1]
		
		if onesConnectedToBorder[row][col]:
			continue
		
		onesConnectedToBorder[row][col] = True
		
		if matrix[row][col] == 0:
			continue
		
		neighbors = getNeighbors(matrix, row, col)
		for neighbor in neighbors:
			stack.append(neighbor)
		
def getNeighbors(matrix, row, col):
	neighbors = []
	if row != 0:
		neighbors.append([row - 1, col])
	if row != len(matrix) - 1:
		neighbors.append([row + 1, col])
	if col != 0:
		neighbors.append([row, col - 1])
	if col != len(matrix[0]) - 1:
		neighbors.append([row, col + 1])
	return neighbors