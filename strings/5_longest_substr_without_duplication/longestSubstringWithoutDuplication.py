# def longestSubstringWithoutDuplication(string):
#     longest = [0, 1]
#     lastSeen = {}
#     startIdx = 0
#     for i, char in enumerate(string):
#         if char in lastSeen:
#             startIdx = max(startIdx, lastSeen[char] + 1)
            
#         currentLongest = [startIdx, i + 1]
#         longest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
            
#         lastSeen[char] = i

#     return string[longest[0] : longest[1]]


def longestSubstringWithoutDuplication(string):
    startIdx = 0
    hashMap = {}
    longestSubString = string[0 : 1]
    for i in range(len(string)):
        if string[i] in hashMap:
            startIdx = max(hashMap[string[i]] + 1, startIdx)
        
        hashMap[string[i]] = i
        currSubString = string[startIdx : i + 1]
        longestSubString = max(longestSubString, currSubString, key = len)
            
            
    return longestSubString


string = "clementisacap"
print(longestSubstringWithoutDuplication(string))
