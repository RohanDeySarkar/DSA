# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
	diameter, _ = helper(tree)
	return diameter

def helper(tree):
	if tree is None:
		return 0, 0
	
	leftDiameter, leftHeight = helper(tree.left)
	rightDiameter, rightHeight = helper(tree.right)
	
	currentDiameter = max(leftDiameter, rightDiameter, leftHeight + rightHeight)
	currentHeight = max(leftHeight, rightHeight) + 1
	
	return currentDiameter, currentHeight
