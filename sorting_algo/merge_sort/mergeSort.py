# O(nlog(n)) time | O(log(n)) space
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    middleIdx = len(arr) // 2
    leftHalf = mergeSort(arr[:middleIdx])
    rightHalf = mergeSort(arr[middleIdx:])
    newArr = mergeSortedArr(leftHalf, rightHalf)
    return newArr

def mergeSortedArr(leftHalf, rightHalf):
    newArr = [] 
    i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] >= rightHalf[j]:
            newArr.append(rightHalf[j])
            j += 1
        elif leftHalf[i] <= rightHalf[j]:
            newArr.append(leftHalf[i])
            i += 1
    if i != len(leftHalf):
        newArr.extend(leftHalf[i:])
    if j != len(rightHalf):
        newArr.extend(rightHalf[j:])
    return newArr
        


arr = [4,3,2,1,6,7,8,9]
print(mergeSort(arr))



    
