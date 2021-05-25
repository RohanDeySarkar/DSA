# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.populateSuffixTrieFrom(string)

	def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingIdx(i, string)

	def insertSubstringStartingIdx(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		# add * at the last node when whole suffix is added
		node["*"] = True

	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return "*" in node


trie = SuffixTrie("babc")
print(trie.root)
