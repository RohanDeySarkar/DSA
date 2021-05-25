# def spiralTraverse(arr):
#     result = []
#     spiralHelper(arr, 0, len(arr) - 1, 0, len(arr[0]) - 1, result)
#     return result

# def spiralHelper(arr, startRow, endRow, startCol, endCol, result):
# 	if startRow > endRow or startCol > endCol:
# 		return

# 	for col in range(startCol, endCol + 1):
# 		result.append(arr[startRow][col])

# 	for row in range(startRow + 1, endRow + 1):
# 		result.append(arr[row][endCol])

# 	for col in reversed(range(startCol, endCol)):
# 		if startRow == endRow:
# 			break
# 		result.append(arr[endRow][col])

# 	for row in reversed(range(startRow + 1, endRow)):
# 		if startCol == endCol:
# 			break
# 		result.append(arr[row][startCol])

# 	spiralHelper(arr, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)
	

def spiralTraverse(arr):
    result = []
    startRow, endRow = 0, len(arr) - 1
    startCol, endCol = 0, len(arr[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(arr[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(arr[row][endCol])

        for col in reversed(range(startCol, endCol)):
            # for [11, 12] same row but diff col
            if startRow == endRow:
                break
            result.append(arr[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(arr[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result


arr = [[1, 2, 3, 4],
       [10, 11, 12, 5],
       [9, 8, 7, 6]]
print(spiralTraverse(arr))
