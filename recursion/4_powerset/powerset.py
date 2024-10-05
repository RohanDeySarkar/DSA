def powerset(arr):
    subsets = [[]]
    for i in range(len(arr)):
        for j in range(len(subsets)):
            subsets.append([arr[i]] + subsets[j])
    return subsets

arr = [1,2,3]
print(powerset(arr))