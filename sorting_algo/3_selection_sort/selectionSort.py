def selectionSort(arr):
    currentIdx = 0
    while currentIdx < len(arr):
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(arr)):
            if arr[smallestIdx] > arr[i] :
                smallestIdx = i
        swap(arr, smallestIdx, currentIdx)
        currentIdx += 1
    return arr

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


arr = [8,5,2,9,5,6,3]
print(selectionSort(arr))
