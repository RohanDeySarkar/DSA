# # O(n) time | O(1) space
def hasSingleCycle(arr):
	nodesVisited = 0
	currentIdx = 0
	while nodesVisited < len(arr):
		# Check for loop at start idx [eg:- [1, -1, 3, 4, 5]]
		if nodesVisited > 0 and currentIdx == 0:
			return False
		nodesVisited += 1
		currentIdx = nextIdx(currentIdx, arr)
	return currentIdx == 0


def nextIdx(currentIdx, arr):
	idx = (currentIdx + arr[currentIdx]) % len(arr)
	return idx




arr = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(arr))
