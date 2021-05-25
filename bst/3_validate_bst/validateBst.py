# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return helper(tree, float("-inf"), float("inf"))

def helper(tree, minValue, maxValue):
	if tree is None:
		return True
	elif tree.value < minValue or tree.value >= maxValue:
		return False

	leftIsValid = helper(tree.left, minValue, tree.value)
	rightIsValid = helper(tree.right, tree.value, maxValue)

	return leftIsValid and rightIsValid