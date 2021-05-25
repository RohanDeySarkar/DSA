# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
	depthTwo = getDepth(topAncestor, descendantTwo)
	if depthOne > depthTwo:
		return getCommon(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return getCommon(descendantTwo, descendantOne, depthTwo - depthOne)
	
def getDepth(topAncestor, descendant):
	depth = 0
	while topAncestor != descendant:
		descendant = descendant.ancestor
		depth += 1
	return depth

def getCommon(higherDepth, lowerDepth, diff):
	while diff != 0:
		higherDepth = higherDepth.ancestor
		diff -= 1
 	# both at same depth, check for same ancestor
	while higherDepth != lowerDepth:
		higherDepth = higherDepth.ancestor
		lowerDepth = lowerDepth.ancestor
	return higherDepth


