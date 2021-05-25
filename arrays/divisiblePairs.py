# Find all possible pairs(sum) divible by n and return the no. of pairs

def div(arr, n):
	left = 0
	right = len(arr) - 1
	pair = 0
	while left < len(arr)-1:
		currNum = arr[left] + arr[right]
		if currNum%n == 0:
			right -= 1
			pair += 1
		elif currNum%n != 0:
			right -= 1
		if right == left-1:
			right = len(arr) - 1
			left += 1
	return pair


arr = [10,9,4,5,7,2,8,20,21]
n = 15
print(div(arr, n))
