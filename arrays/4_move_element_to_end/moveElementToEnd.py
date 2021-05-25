# O(n) time | O(1) space
def moveElementToEnd(arr, toMove):
    left = 0
    right = len(arr) - 1 
    while left < right:
        while left < right and arr[right] == toMove:
            right -= 1
        if arr[left] == toMove:
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
    
    return arr


arr = [3,1,2,4,5,3,3]
toMove = 3
print(moveElementToEnd(arr, toMove))
