def longestIncreasingSubsequence(arr):
	lengths = [1 for i in arr]
	sequences = [None for i in arr]
	maxLengthIdx = 0
	for i in range(len(arr)):
		currentNum = arr[i]
		for j in range(0, i):
			prevNum = arr[j]
			if prevNum < currentNum and lengths[j] + 1 >= lengths[i]:
				lengths[i] = lengths[j] + 1
				sequences[i] = j
		if lengths[i] >= lengths[maxLengthIdx]:
			maxLengthIdx = i
	
	sequence = []
	currentIdx = maxLengthIdx
	while currentIdx is not None:
		sequence.append(arr[currentIdx])
		currentIdx = sequences[currentIdx]
		
	return list(reversed(sequence))
