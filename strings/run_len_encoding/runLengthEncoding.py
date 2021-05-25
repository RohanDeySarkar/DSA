def runLengthEncoding(string):
	encodedString = []
	prevChar = string[0]
	count = 1
	for i in range(1, len(string)):
		currentChar = string[i]
		if currentChar == prevChar and count != 9:
			prevChar = currentChar
			count += 1
		else:
			encodedString.append(str(count)+prevChar)
			count = 1
			prevChar = currentChar

	encodedString.append(str(count)+prevChar)
	
	return "".join(encodedString)


string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))
