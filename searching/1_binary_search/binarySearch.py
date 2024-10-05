def binarySearch(arr, target):
	return helper(arr, target, 0, len(arr)-1)

# O(log(n)) time space
def helper(arr, target, left, right):
	if left > right or right < left:
		return -1
	middle = (left + right) // 2
	currentNum = arr[middle]
	if target == currentNum:
		return middle
	elif target > currentNum:
		return helper(arr, target, middle+1, right)
	else:
		return helper(arr, target, left, middle-1)

# O(log(n)) time | O(1) space
def binarySearch(arr, target):
    left = 0
	right = len(arr) - 1
	while left <= right:
		middle = (left+right) // 2
		num = arr[middle]
		if target == num:
			return middle
		elif target > num:
			left = middle +1
		else:
			right = middle - 1
	return -1

arr = [1,2,3,4,5,6]
target = 90
print(binarySearch(arr, target))
