def subsetSum(total, arr):
    return helper(total, arr, len(arr) - 1)

def helper(total, arr, idx):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif idx < 0:
        return 0
    elif arr[idx] > total:
        return helper(total, arr, idx - 1)
    else:
        currSum = helper(total - arr[idx], arr, idx - 1)
        nextSum = helper(total, arr, idx - 1)
        
        return  currSum + nextSum


# numways dp problem

n = 6
arr = [2,4,6,10]
print(subsetSum(n, arr))
