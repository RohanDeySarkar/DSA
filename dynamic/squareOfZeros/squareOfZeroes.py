# The given matrix will have same no. of rows & cols
def squareOfZeroes(matrix):
    n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				bottomRow = topRow - 1 + squareLength
				rightCol = leftCol - 1 + squareLength
				if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False
			
def isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
	for row in range(topRow, bottomRow + 1):
		if matrix[row][leftCol] != 0 or matrix[row][rightCol] != 0:
			return False
	for col in range(leftCol, rightCol + 1):
		if matrix[topRow][col] != 0 or matrix[bottomRow][col] != 0:
			return False
	return True
