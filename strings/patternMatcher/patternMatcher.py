def patternMatcher(pattern, string):
	if len(pattern) > len(string):
		return []
	# yyxyyx -> xxyxxy if any
	newPattern = getNewPattern(pattern)
	didSwitch = newPattern[0] != pattern[0]
	counts = {"x": 0, "y": 0}
	
	firstYPos = getCountsAndFirstYPos(newPattern, counts)
	
	if counts["y"] != 0:
		for lenOfX in range(1, len(string)):
			lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
			# check lenOfY is not -ve and not contains decimal vals
			if lenOfY <= 0 or lenOfY % 1 != 0:
				continue
				
			lenOfY = int(lenOfY)
			yIdx = firstYPos * lenOfX
			
			x = string[:lenOfX]
			y = string[yIdx: yIdx + lenOfY]
			
			match = map(lambda char: x if char == "x" else y, newPattern)
			
			if string == "".join(match):
				return [x, y] if not didSwitch else [y, x]
	else:
		lenOfX = len(string) / counts["x"]
		if lenOfX % 1 == 0:
			lenOfX = int(lenOfX)
			x = string[:lenOfX]
			
			match = map(lambda char: x, newPattern)
			
			if string == "".join(match):
				return [x, ""] if not didSwitch else ["", x]
	return []
	
def getNewPattern(pattern):
	patternLetters = list(pattern)
	if pattern[0] == "x":
		return patternLetters
	else:
		return list(map(lambda char: "x" if char == "y" else "y", patternLetters))
	
	
def getCountsAndFirstYPos(pattern, counts):
	firstYPos = None
	for i, char in enumerate(pattern):
		counts[char] += 1
		if firstYPos is None and char == "y":
			firstYPos = i
	return firstYPos





















