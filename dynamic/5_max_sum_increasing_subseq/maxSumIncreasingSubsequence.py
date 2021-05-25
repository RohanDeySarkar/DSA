def maxSumIncreasingSubsequence(arr):
    sums = [num for num in arr]
    sequences = [None for i in arr]
    maxSumIdx = 0
    for i in range(len(arr)):
        currentNum = arr[i]
        for j in range(0, i):
            prevNum = arr[j]
            if currentNum > prevNum and currentNum + sums[j] > sums[i]:
                sums[i] = currentNum + sums[j]
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
            
    sequence = []
    currentMaxSumIdx = maxSumIdx
    while currentMaxSumIdx is not None:
        sequence.append(arr[currentMaxSumIdx])
        currentMaxSumIdx = sequences[currentMaxSumIdx]
        
    sequence = list(reversed(sequence))
    
    return [sums[maxSumIdx], sequence]


arr = [8,12,2,3,15,5,7]
print(maxSumIncreasingSubsequence(arr))
