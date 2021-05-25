def groupAnagrams(words):  
    anagrams = {}
    for word in words:
    	sortedWord = "".join(sorted(word))
    	# print(sortedWord)
    	if sortedWord not in anagrams:
    		anagrams[sortedWord] = [word]
    	else:
    		anagrams[sortedWord].append(word)

    return list(anagrams.values())


words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
print(groupAnagrams(words))
