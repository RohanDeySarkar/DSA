def rightSmallerThan(arr):
	rightSmallerArr = []
	for i in range(len(arr)):
		rightSmallCount = 0
		currElem = arr[i]
		for j in range(i + 1, len(arr)):
			nextElem = arr[j]
			if currElem > nextElem:
				rightSmallCount += 1
		rightSmallerArr.append(rightSmallCount)
	return rightSmallerArr
