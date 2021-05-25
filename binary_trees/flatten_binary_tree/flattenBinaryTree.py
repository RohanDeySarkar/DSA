# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def flattenBinaryTree(root):
    arr = inOrderTraverse(root, [])
	if len(arr) == 1:
		return arr[0]
	for i in range(0, len(arr)):
		if i == 0 :
			arr[0].right = arr[1]
		elif i == len(arr) - 1:
			arr[len(arr) - 1].left = arr[len(arr) - 2]
		else:
			arr[i].left = arr[i - 1]
			arr[i].right = arr[i + 1]
	return arr[0]


# A little optimal
def flattenBinaryTree(root):
    arr = inOrderTraverse(root, [])
	for i in range(0, len(arr) - 1):
		leftNode = arr[i]
		rightNode = arr[i + 1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return arr[0]
	
	
def inOrderTraverse(node, arr):
	if node is not None:
		inOrderTraverse(node.left, arr)
		arr.append(node)
		inOrderTraverse(node.right, arr)
	return arr