def searchForRange(arr, target):
    finalRange = [-1,-1]
    helper(arr, target, 0, len(arr)-1, finalRange, True)
    helper(arr, target, 0, len(arr)-1, finalRange, False)
    return finalRange

def helper(arr, target, left, right, finalRange, goLeft):
    if left > right:
        return
    
    mid = (left+right) // 2
    
    if arr[mid] > target:
        helper(arr, target, left, mid-1, finalRange, goLeft)
    elif arr[mid] < target:
        helper(arr, target, mid+1, right, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or arr[mid-1] != target:
                finalRange[0] = mid
            else:
                helper(arr, target, left, mid-1, finalRange, goLeft)
        else:
            if mid == len(arr)-1 or arr[mid+1] != target:
                finalRange[1] = mid
            else:
                helper(arr, target, mid+1, right, finalRange, goLeft)
        


arr= [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
print(searchForRange(arr, target))
