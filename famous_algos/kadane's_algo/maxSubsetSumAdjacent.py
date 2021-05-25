# O(1) space
def kadanesAlgorithm(arr):
    prevSums = arr[0]
    maxSum = arr[0]
    for i in range(1, len(arr)):
        currentNum = arr[i]
        prevSums = max(currentNum + prevSums, currentNum)
        maxSum = max(maxSum, prevSums)
    return maxSum
    
# O(n) space
def kadanesAlgorithm(arr):
    sums = [num for num in arr]
    for i in range(1, len(arr)):
        currentNum = arr[i]
        sums[i] = max(sums[i-1] + currentNum, currentNum)
    return max(sums)


arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(arr))
