def multiStringSearch(bigString, smallStrings):
    allCombinations = []
	for i in range(len(bigString)):
		for j in range(i, len(bigString)):
			allCombinations.append(bigString[i : j + 1])
	output = []
	for smallString in smallStrings:
		if smallString in allCombinations:
			output.append(True)
		else:
			output.append(False)
			
	return output


# Trie approach
# O(ns + bs) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
		
	containedStrings = {}
	
	for i in range(len(bigString)):
		checkForSmallStrings(i, bigString, trie, containedStrings)
		
	return [string in containedStrings for string in smallStrings]
		
	
def checkForSmallStrings(startIdx, bigString, trie, containedStrings):
	currentNode = trie.root
	for i in range(startIdx, len(bigString)):
		currentChar = bigString[i]
		if currentChar not in currentNode:
			break
			
		currentNode = currentNode[currentChar]
		
		if "*" in currentNode:
			containedStrings[currentNode["*"]] = True
	
	
class Trie:
	def __init__(self):
		self.root = {}
	
	def insert(self, string):
		current = self.root
		for i in range(len(string)):
			if string[i] not in current:
				current[string[i]] = {}
			current = current[string[i]]
		current["*"] = string