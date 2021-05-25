def inOrderTraverse(tree, arr):
    if tree is not None:
    	inOrderTraverse(tree.left, arr)
    	arr.append(tree.value)
    	inOrderTraverse(tree.right, arr)
    return arr

def preOrderTraverse(tree, arr):
    if tree is not None:
    	arr.append(tree.value)
    	preOrderTraverse(tree.left, arr)
    	preOrderTraverse(tree.right, arr)
    return arr

def postOrderTraverse(tree, arr):
	if tree is not None:
		postOrderTraverse(tree.left, arr)
		postOrderTraverse(tree.right, arr)
		arr.append(tree.value)
	return arr
    
