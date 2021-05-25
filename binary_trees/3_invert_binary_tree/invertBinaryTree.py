def invertBinaryTree(tree):
	if tree is None:
		return 
    tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	return tree


# queue
def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		currentNode = queue.pop(0)
		if currentNode is None:
			continue
		currentNode.left, currentNode.right = currentNode.right, currentNode.left
		queue.append(currentNode.left)
		queue.append(currentNode.right)
	return tree
	

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
