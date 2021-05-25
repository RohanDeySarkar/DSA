def staircaseTraversal(height, maxSteps):
    steps = [0 for _ in range(height + 1)]
	steps[0] = 1
	steps[1] = 1
	for currHeight in range(2, height + 1):
		step = 1
		while step <= maxSteps:
			steps[currHeight] += steps[currHeight - step]
			step += 1
		
	return steps[-1]
