def powerset(arr):
    subsets = [[]]
    for element in arr:
        for i in range(len(subsets)):
            currSubset = subsets[i]
            subsets.append(currSubset + [element])
            
    return subsets
        

arr = [1,2,3]
print(powerset(arr))
