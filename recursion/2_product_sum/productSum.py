# O(n) time | O(d) space
# n => total no. of elements in the arr
# d => greatest depth of "special arr" in the arr

def productSum(arr):
    multiplier = 1
    return helper(arr, multiplier)

def helper(arr, multiplier):
    totalSum = 0
    for element in arr:
        if type(element) is list:
            totalSum += helper(element, multiplier + 1)
        else:
            totalSum += element
            
    return totalSum * multiplier

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))
