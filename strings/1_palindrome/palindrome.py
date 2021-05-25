#def isPalindrome(string):
#    return True if string == string[::-1] else False

# O(n) time | O(1) space
def isPalindrome(string):
	left = 0
	right = len(string) - 1
	while left < right:
		if string[left] == string[right]:
			left += 1
			right -= 1
		else:
			return False
	return True

string = "abcdcba"
print(isPalindrome(string))
