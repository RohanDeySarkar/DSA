def longestCommonSubsequence(str1, str2):
    lcs = [[[] for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]
	for row in range(1, len(str1) + 1):
		str1Word = str1[row - 1]
		for col in range(1, len(str2) + 1):
			str2Word = str2[col - 1]
			if str1Word == str2Word:
				lcs[row][col] = lcs[row - 1][col - 1] + [str2Word]
			else:
				lcs[row][col] = max(lcs[row][col - 1], lcs[row - 1][col], key=len)
	return lcs[-1][-1]


str1 = "xkykzpw"
str2 = "zxvvyzw"
print(longestCommonSubsequence(str1, str2))
