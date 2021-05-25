def longestBalancedSubstring(string):
	maxLength = 0
	for i in range(len(string)):
		for j in range(i, len(string) + 1):
			if isBalanced(string[i : j]):
				currLength = j - i
				maxLength = max(maxLength, currLength)
	return maxLength
		
def isBalanced(string):
	stack = []
	for char in string:
		if char == "(":
			stack.append("(")
		elif len(stack) > 0:
			stack.pop()
		else: 
			return False
	return len(stack) == 0




# O(n)
def longestBalancedSubstring(string):
	idxStack = [-1]
	maxLength = 0
	for idx in range(len(string)):
		if string[idx] == "(":
			idxStack.append(idx)
		else:
			idxStack.pop()
			if len(idxStack) == 0:
				idxStack.append(idx)
			else:
				balanceStartIdx = idxStack[-1]
				currLength = idx - balanceStartIdx
				maxLength = max(maxLength, currLength)
	return maxLength




string = "(()))("
print(longestBalancedSubstring(string))

