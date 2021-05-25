# Using insert function
def minHeightBst(arr):
	return helper(0, len(arr) - 1, arr, None)

def helper(startIdx, endIdx, arr, bst):
	if startIdx > endIdx:
		return None
	midIdx = (startIdx + endIdx) // 2
	if bst is None:
		bst = BST(arr[midIdx])
	else:
		bst.insert(arr[midIdx])
	helper(startIdx, midIdx - 1, arr, bst)
	helper(midIdx + 1, endIdx, arr, bst)
	return bst


# Without using insert function [O(n) space | time]
def minHeightBst(arr):
	return helper(0, len(arr) - 1, arr)

def helper(startIdx, endIdx, arr):
	if startIdx > endIdx:
		return None
	midIdx = (startIdx + endIdx) // 2
	bst = BST(arr[midIdx])
	bst.left = helper(startIdx, midIdx - 1, arr)
	bst.right = helper(midIdx + 1, endIdx, arr)
	return bst 


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
