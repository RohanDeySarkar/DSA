def indexEqualsValue(arr):
    for idx in range(len(arr)):
		if idx == arr[idx]:
			return idx
	return -1


def indexEqualsValue(arr):
    leftIdx = 0
	rightIdx = len(arr) - 1
	
	while leftIdx <= rightIdx:
		# Integer overflow
		# middleIdx = (leftIdx + rightIdx) // 2
		middleIdx = leftIdx + (rightIdx - leftIdx) // 2
		middleVal = arr[middleIdx]
		
		if middleVal < middleIdx:
			leftIdx = middleIdx + 1
		elif middleVal == middleIdx and middleIdx == 0:
			return middleIdx
		elif middleVal == middleIdx and arr[middleIdx - 1] < middleIdx - 1:
			return middleIdx
		else:
			rightIdx = middleIdx - 1
			
	return -1
