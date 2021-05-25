def maxPathSum(tree):
	_, maxPathSum = helper(tree)
    return maxPathSum
	
def helper(node):
	if node is None:
		return 0, float("-inf")
	
	leftSumAsBranch, leftMaxPathSum = helper(node.left)
	rightSumAsBranch, rightMaxPathSum = helper(node.right)
	maxChildSumAsBranch = max(leftSumAsBranch, rightSumAsBranch)
	
	value = node.value
	
	maxSumAsBranch = max(value, maxChildSumAsBranch + value)
	
	maxSumAsTriangle = max(maxSumAsBranch, leftSumAsBranch + value + rightSumAsBranch)
	maxPathSum = max(maxSumAsTriangle, leftMaxPathSum, rightMaxPathSum)
	
	return maxSumAsBranch, maxPathSum
	
