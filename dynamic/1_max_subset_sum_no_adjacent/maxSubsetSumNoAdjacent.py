# O(n) space
def maxSubsetSumNoAdjacent(arr):
	if not len(arr):
		return 0
	if len(arr) == 1:
        return arr[0]
	maxSums = [num for num in arr]
	maxSums[1] = max(maxSums[0], maxSums[1])
	for i in range(2, len(arr)):
		maxSums[i] = max(arr[i] + maxSums[i - 2], maxSums[i - 1])
	return maxSums[-1]



# O(1) space
def maxSubsetSumNoAdjacent(arr):
    if not len(arr):
        return 0
    if len(arr) == 1:
        return arr[0]
    first = arr[0]
    second = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(arr[i] + first, second)
        first = second
        second = current
    return second


arr = [7,10,12,7,9,14]
print(maxSubsetSumNoAdjacent(arr))
