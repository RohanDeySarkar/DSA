def subarraySort(arr):
    maxNum = float("-inf")
    minNum = float("inf")
    for i in range(len(arr)):
        num = arr[i]
        if isOutOfOrder(num, i, arr):
            maxNum = max(num, maxNum)
            minNum = min(num, minNum)

    if minNum == float("inf"):
        return [-1, -1]

    leftIdx = 0
    while minNum >= arr[leftIdx]:
        leftIdx += 1

    rightIdx = len(arr) - 1
    while maxNum <= arr[rightIdx]:
        rightIdx -= 1
            
    return [leftIdx, rightIdx]
        
def isOutOfOrder(num, idx, arr):
    if idx == 0:
        return num > arr[idx + 1]
    if idx == len(arr) - 1:
        return num < arr[idx - 1]
    return num < arr[idx - 1] or num > arr[idx + 1]


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(arr))
