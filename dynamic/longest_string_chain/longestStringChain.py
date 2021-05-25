def longestStringChain(strings):
    stringChains = {}
	for string in strings:
		stringChains[string] = {"nextString": "", "maxChainLength": 1}
	
	sortedStrings = sorted(strings, key=len)
	for string in sortedStrings:
		findLongestStringChain(string, stringChains)
		
	# find which one has the longest chain length
	maxChainLength = 0
	startChain = ""
	for string in strings:
		if stringChains[string]["maxChainLength"] > maxChainLength:
			maxChainLength = stringChains[string]["maxChainLength"]
			startChain = string
			
	# build the sequence
	sequence = []
	currentString = startChain
	while currentString != "":
		sequence.append(currentString)
		currentString = stringChains[currentString]["nextString"]
	
	return [] if len(sequence) == 1 else sequence

def findLongestStringChain(string, stringChains):
	for i in range(len(string)):
		smallerString = string[0 : i] + string[i + 1 : ]
		if smallerString not in stringChains:
			continue
			
		smallerStringLength = stringChains[smallerString]["maxChainLength"]
		currentStringLength = stringChains[string]["maxChainLength"]
		
		if smallerStringLength + 1 > currentStringLength:
			stringChains[string]["maxChainLength"] = smallerStringLength + 1
			stringChains[string]["nextString"] = smallerString
