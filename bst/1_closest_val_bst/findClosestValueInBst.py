# Using recursion
def findClosestValueInBst(tree, target):
	return helper(tree, target, tree.value)

def helper(currentNode, target, closest):
	if currentNode is None:
		return closest
	if abs(target - currentNode.value) < abs(target - closest):
		closest = currentNode.value
	if target > currentNode.value:
		return helper(currentNode.right, target, closest)
	elif target < currentNode.value:
		return helper(currentNode.left, target, closest)
	else:
		return closest


# Without recursion
def findClosestValueInBst(tree, target):
    currentNode = tree
	closest = tree.value
	while currentNode is not None:
		if abs(target - currentNode.value) < abs(target - closest):
			closest = currentNode.value
		if target > currentNode.value:
			currentNode = currentNode.right
		elif target < currentNode.value:
			currentNode = currentNode.left
		else:
			break
	
	return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
