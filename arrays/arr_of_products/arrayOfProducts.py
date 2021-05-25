# def arrayOfProducts(arr):
# 	products = []
# 	for i in range(len(arr)):
# 		runningProduct = 1
# 		for j in range(len(arr)):
# 			if i != j:
# 				runningProduct *= arr[j]
# 		products.append(runningProduct)
# 	return products



# similar -- > water area problem
# O(n) time | space
def arrayOfProducts(arr):
	leftProducts = [1 for _ in arr]
	leftRunningProduct = 1
	for i in range(len(arr)):
		leftProducts[i] = leftRunningProduct
		leftRunningProduct *= arr[i]

	rightProducts = [1 for _ in arr]
	rightRunningProduct = 1
	for i in reversed(range(len(arr))):
		rightProducts[i] = rightRunningProduct
		rightRunningProduct *= arr[i]

	products = [1 for _ in arr]
	for i in range(len(arr)):
		products[i] = leftProducts[i] * rightProducts[i]

	return products




arr = [5, 1, 4, 2]
print(arrayOfProducts(arr))	