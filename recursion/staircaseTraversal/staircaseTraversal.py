def staircaseTraversal(height, maxSteps):
    numWays = [0 for _ in range(height + 1)]
	numWays[0] = 1
	numWays[1] = 1
	for currHeight in range(2, height + 1):
		step = 1
		while step <= maxSteps:
			numWays[currHeight] += numWays[currHeight - step]
			step += 1
		
	return numWays[-1]


# Alternate
def staircaseTraversal(height, maxSteps):
    steps = [0 for _ in range(height + 1)]
    steps[0] = 1
    for i in range(height + 1):
        for j in range(1, maxSteps + 1):
            if j <= i:
                steps[i] += steps[ i - j]
    return steps[-1]
