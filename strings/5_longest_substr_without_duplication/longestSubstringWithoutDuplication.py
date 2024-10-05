def longestSubstringWithoutDuplication(string):
    longest = [0, 1]
    lastSeen = {}
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
            
        currentLongest = [startIdx, i + 1]
        longest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
            
        lastSeen[char] = i

    return string[longest[0] : longest[1]]


string = "clementisacap"
print(longestSubstringWithoutDuplication(string))
