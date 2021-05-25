# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


		
def findSuccessor(tree, node):
    arr = helper(tree, node, [])
	targetIdx = None
	for i in range(len(arr)):
		if node == arr[i]:
			if i + 1 < len(arr):
				targetIdx = i + 1
	return arr[targetIdx] if targetIdx != None else targetIdx
	
def helper(tree, node, arr):
	if tree is not None:
		helper(tree.left, node, arr)
		arr.append(tree)
		helper(tree.right, node, arr)
	return arr
