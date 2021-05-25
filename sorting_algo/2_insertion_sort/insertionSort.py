def insertionSort(arr):
    for i in range(1, len(arr)):
        currentIdx = i
        while currentIdx > 0 and arr[currentIdx] < arr[currentIdx - 1]:
            swap(arr, currentIdx, currentIdx - 1)
            currentIdx -= 1
    return arr

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

arr = [8,5,2,9,5,6,3]
print(insertionSort(arr))
