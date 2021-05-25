def quickSelect(arr, k):
    position = k - 1
    return helper(arr, 0, len(arr) - 1, position)

def helper(arr, startIdx, endIdx, position):
    while True:
        if startIdx >= endIdx:
            print('Search completed:')
            
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        
        while leftIdx <= rightIdx:
            if arr[pivotIdx] < arr[leftIdx] and arr[pivotIdx] > arr[rightIdx]:
                swap(arr, leftIdx, rightIdx)
            if arr[pivotIdx] > arr[leftIdx]:
                leftIdx += 1
            if arr[pivotIdx] < arr[rightIdx]:
                rightIdx -= 1
                
        swap(arr, pivotIdx, rightIdx)
        
        if rightIdx == position:
            return arr[rightIdx]
        elif rightIdx > position:
            endIdx = rightIdx - 1
        else:
            startIdx = rightIdx + 1
    

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr
    

arr = [8,5,2,9,7,6,3]
k = 3
print(quickSelect(arr, k))
