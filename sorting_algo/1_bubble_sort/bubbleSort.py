# def bubbleSort(arr):
#     notSorted = True
#     while notSorted:
#         idx = 0
#         notSorted = False
#         while idx < len(arr) - 1:
#             if arr[idx] > arr[idx+1]:
#                 swap(arr, idx, idx + 1)
#                 notSorted = True
#             idx += 1                  
#     return arr

def bubbleSort(arr):
	notSorted = True
	counter = 0
	while notSorted:
		notSorted = False
		for i in range(len(arr) - 1 - counter):
			if arr[i] > arr[i + 1]:
				swap(arr, i, i + 1)
				notSorted = True
			counter += 1
	return arr

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]                 
                              
    
arr = [8,5,2,9,5,6,3]
print(bubbleSort(arr))
