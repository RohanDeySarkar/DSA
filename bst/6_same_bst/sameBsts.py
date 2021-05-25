def sameBsts(arrOne, arrTwo):
	if len(arrOne) != len(arrTwo):
		return False
	if len(arrOne) == 0 and len(arrTwo) == 0:
		return True
	if arrOne[0] != arrTwo[0]:
		return False
	
	leftOne, rightOne = getNodes(arrOne)
	leftTwo, rightTwo = getNodes(arrTwo)
	
	leftNodeValid = sameBsts(leftOne, leftTwo)
	rightNodeValid = sameBsts(rightOne, rightTwo)
	
	return leftNodeValid and rightNodeValid
	
def getNodes(arr):
	left = []
	right = []
	head = arr[0]
	for i in range(1, len(arr)):
		if arr[i] >= head:
			right.append(arr[i])
		else:
			left.append(arr[i])
	return left, right





arrOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(arrOne, arrTwo))



