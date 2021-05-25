# O(n) time space
# def twoNumberSum(array, targetSum):
# 	nums = {}
# 	for num in array:
# 		y = targetSum - num
# 		if y in nums:
# 			return [y, num]
# 		else:
# 			nums[num] = True
# 	return []

# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		currentsum = array[left] + array[right]
		if currentsum == targetSum:
			return [array[left], array[right]]
		elif currentsum > targetSum:
			right -= 1
		elif currentsum < targetSum:
			left += 1
	return []

array = [3,5,-4,8,11,-1,1,6]
targetSum = 13

print(twoNumberSum(array, targetSum))
