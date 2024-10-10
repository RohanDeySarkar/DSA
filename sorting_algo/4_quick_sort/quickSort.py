# O(nlog(n)) time | O(log(n)) space
def quickSort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr

def helper(arr, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    
    while leftIdx <= rightIdx:
        if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
            swap(leftIdx, rightIdx, arr)
        if arr[leftIdx] <= arr[pivotIdx]:
            leftIdx += 1
        if arr[rightIdx] >= arr[pivotIdx]:
            rightIdx -= 1
            
    swap(pivotIdx, rightIdx, arr)

    leftSubarrIsSmaller = rightIdx - 1 - startIdx < endIdx - rightIdx + 1
    
    if leftSubarrIsSmaller:
        helper(arr, startIdx, rightIdx - 1)
        helper(arr, rightIdx + 1, endIdx)
    else:
        helper(arr, rightIdx + 1, endIdx)
        helper(arr, startIdx, rightIdx - 1)

def swap(idx1, idx2, arr):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

#arr = [8,5,2,9,5,6,3]
arr = [1,3,2]
print(quickSort(arr))
