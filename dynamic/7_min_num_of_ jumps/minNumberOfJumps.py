def minNumberOfJumps(arr):
    jumps = [float("inf") for x in arr]
    jumps[0] = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] >= i - j:
                jumps[i] = min(jumps[j] + 1, jumps[i])
                
    return jumps[-1]

arr = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps(arr))
