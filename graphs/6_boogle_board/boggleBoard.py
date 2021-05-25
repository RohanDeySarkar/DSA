def boggleBoard(board, words):
    trie = Trie()
	for word in words:
		trie.add(word)
	
	visited = [[False for col in row] for row in board]
	finalWords = []
	
	for i in range(len(board)):
		for j in range(len(board[0])):
			explore(i, j, board, visited, finalWords, trie.root)
			
	return finalWords

def explore(i, j, board, visited, finalWords, trieNode):
	if visited[i][j]:
		return
	letter = board[i][j]
	if letter not in trieNode:
		return
	visited[i][j] = True
	trieNode = trieNode[letter]
	if "*" in trieNode:
		if trieNode["*"] not in finalWords:
			finalWords.append(trieNode["*"])
	neighbors = getNeighbors(i, j, board)
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, visited, finalWords, trieNode)
	visited[i][j] = False
		
def getNeighbors(i, j, board):
	neighbors = []
	if i > 0  and j > 0:
		neighbors.append([i - 1, j - 1])
	if i > 0:
		neighbors.append([i - 1, j])
	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i - 1, j + 1])
		
	if j < len(board[0]) - 1:
		neighbors.append([i, j + 1])
	if j > 0:
		neighbors.append([i, j - 1])
		
	if i < len(board) - 1 and j > 0:
		neighbors.append([i + 1, j - 1])
	if i < len(board) - 1:
		neighbors.append([i + 1, j])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i + 1, j + 1])
	return neighbors
	
class Trie:
	def __init__(self):
		self.root = {}
		
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current["*"] = word