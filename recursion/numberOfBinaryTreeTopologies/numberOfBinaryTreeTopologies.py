def numberOfBinaryTreeTopologies(n, cache={0 : 1}):
    if n in cache:
		return cache[n]
	numOfTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - leftTreeSize - 1
		numofLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
		numofRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
		numOfTrees += numofLeftTrees * numofRightTrees
	cache[n] = numOfTrees
	return cache[n]
