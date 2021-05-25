def getPermutations(arr):
    permutations = []
    currentPermutation = []
    helper(arr, currentPermutation, permutations)
    return permutations

def helper(arr, currentPermutation, permutations):
    if len(arr) == 0:
        return permutations.append(currentPermutation)
    else:
        for i in range(len(arr)):
            newArr = arr[:i] + arr[i+1:]
            newPermutation = currentPermutation + [arr[i]]
            helper(newArr, newPermutation, permutations)


arr = [1,2,3]
print(getPermutations(arr))
