# Similar to maxSumIncreasingSubseq problem

def diskStacking(disks):
	# disks.sort(key=lambda disk: disk[2])
	disks = sorted(disks, key=lambda disk: disk[2])
	heights = [disk[2] for disk in disks]
	sequences = [None for disk in disks]

	maxHeightIdx = 0

	for i in range(1, len(disks)):
		currentDisk = disks[i]
		for j in range(0, i):
			otherDisk = disks[j]
			if isValidDimensions(otherDisk, currentDisk):
				if currentDisk[2] + heights[j] >= heights[i]:
					heights[i] = currentDisk[2] + heights[j]
					sequences[i] = j

		if heights[i] >= heights[maxHeightIdx]:
			maxHeightIdx = i

	sequence = []
	currentIdx = maxHeightIdx
	while currentIdx is not None:
		sequence.append(disks[currentIdx])
		currentIdx = sequences[currentIdx]

	return list(reversed(sequence))

def isValidDimensions(otherDisk, currentDisk):
	return otherDisk[0] < currentDisk[0] and otherDisk[1] < currentDisk[1] and otherDisk[2] < currentDisk[2] 



disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
print(diskStacking(disks))
