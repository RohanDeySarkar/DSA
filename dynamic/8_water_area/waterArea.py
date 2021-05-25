def waterArea(heights):
	if len(heights) == 0:
		return 0
		
    leftMax = [0 for h in heights]
    leftMax[0] = heights[0]

    for i in range(1, len(heights)):
        leftMax[i] = max(heights[i], leftMax[i - 1])
        
    rightMax = [0 for h in heights]
    rightMax[len(heights) - 1] = heights[-1]

    for i in reversed(range(len(heights) - 1)):
        rightMax[i] = max(rightMax[i + 1], heights[i])

    maxes = [0 for h in heights]
    
    for i in range(len(heights)):
        minHeight = min(leftMax[i], rightMax[i])
        maxes[i] = minHeight - heights[i]

    return sum(maxes)


def waterArea(heights):
	if len(heights) == 0:
		return 0

	leftIdx = 0
	rightIdx = len(heights) - 1

	leftMax = heights[leftIdx]
	rightMax = heights[rightIdx]

	surfaceArea = 0

	while leftIdx < rightIdx:
		if heights[rightIdx] > heights[leftIdx]:
			leftMax = max(leftMax, heights[leftIdx])
			surfaceArea += leftMax - heights[leftIdx]
			leftIdx += 1
		else:
			rightMax = max(rightMax, heights[rightIdx])
			surfaceArea += rightMax - heights[rightIdx]
			rightIdx -= 1
			
	return surfaceArea


    
h = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(h))
