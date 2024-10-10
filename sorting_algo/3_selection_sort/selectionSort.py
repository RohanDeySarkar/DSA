# def selectionSort(arr):
#     currentIdx = 0
#     while currentIdx < len(arr):
#         smallestIdx = currentIdx
#         for i in range(currentIdx + 1, len(arr)):
#             if arr[smallestIdx] > arr[i]:
#                 smallestIdx = i
#         swap(arr, smallestIdx, currentIdx)
#         currentIdx += 1
#     return arr

# def swap(arr, idx1, idx2):
#     arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


# O(n^2) time | O(1) space
def selectionSort(arr):
    for i in range(len(arr)):
        currIdx = i
        currSmallestIdx = currIdx
        for j in range(currIdx + 1, len(arr)):
            if arr[currSmallestIdx] > arr[j]:
                currSmallestIdx = j
        arr[currIdx], arr[currSmallestIdx] = arr[currSmallestIdx], arr[currIdx]
    return arr


arr = [8,5,2,9,5,6,3]
print(selectionSort(arr))
