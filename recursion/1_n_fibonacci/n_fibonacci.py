# O(n) time space
##def getNthFib(n):
#	memoize = {1:0, 2:1}
#	return helper(n, memoize)
#
#def helper(n, memoize):
#	if n in memoize:
#		return memoize[n]
#	else:
#		memoize[n] = helper(n-1, memoize) + helper(n-2, memoize)
#		return memoize[n]

# O(n) time | O(1) space	
def getNthFib(n):
	lastTwo = [0, 1]
	counter = 3
	while n >= counter:
		newNum = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = newNum
		counter += 1
	if n > 1:
		return lastTwo[1]
	else:
		return lastTwo[0]

print(getNthFib(5))
