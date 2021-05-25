# O(n) time space
def largestRange(arr):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in arr:
        nums[num] = True
    for num in arr:
        if nums[num] == False:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1, right-1]
    return bestRange


arr = [1,11,3,0,15,5,2,4,10,7,12,6]
print(largestRange(arr))
