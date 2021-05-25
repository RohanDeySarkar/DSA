def caesarCipherEncryptor(string, key):
	key = key % 26
	result = []
	for letter in string:
		ordVal = ord(letter)
		newOrdVal = ordVal + key
		if newOrdVal <= 122:
			result.append(chr(newOrdVal))
		elif newOrdVal > 122:
			# newOrdVal = (newOrdVal - 122) + 96
			newOrdVal = (newOrdVal % 122) + 96
			result.append(chr(newOrdVal))
	return "".join(result)


string = "abc"
key = 57
print(caesarCipherEncryptor(string, key))
