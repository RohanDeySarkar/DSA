def shiftedBinarySearch(arr, target):
    leftIdx = 0
    rightIdx = len(arr) - 1
    return searchHelper(arr, target, leftIdx, rightIdx)

def searchHelper(arr, target, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    
    middleIdx = (leftIdx + rightIdx) // 2

    potentialMatch = arr[middleIdx]

    leftNum = arr[leftIdx]
    rightNum = arr[rightIdx]

    if target == potentialMatch:
        return middleIdx
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            return searchHelper(arr, target, leftIdx, middleIdx - 1)
        else:
            return searchHelper(arr, target, middleIdx + 1, rightIdx)
    else:
        if target > potentialMatch and target <= rightNum:
            return searchHelper(arr, target, middleIdx + 1, rightIdx)
        else:
            return searchHelper(arr, target, leftIdx, middleIdx - 1)


arr = [61, 71, 72, 73, 0, 1, 21, 33, 45, 45]
##arr = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
target = 33
print(shiftedBinarySearch(arr, target))
