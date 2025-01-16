# O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers

# def numbersInPi(pi, numbers):
#     minSpaces = getMinSpaces(pi, numbers, {}, 0)
#     return -1 if minSpaces == float("inf") else minSpaces

# def getMinSpaces(pi, numbers, cache, idx):
#     if idx == len(pi):
#         return -1
#     if idx in cache:
#         return cache[idx]
#     minSpaces = float("inf")
#     for i in range(idx, len(pi)):
#         prefix = pi[idx : i + 1]
#         if prefix in numbers:
#             minSpacesInSuffix = getMinSpaces(pi, numbers, cache, i + 1)
#             minSpaces = min(minSpaces, minSpacesInSuffix + 1)
#     cache[idx] = minSpaces
#     return cache[idx]



def numbersInPi(pi, numbers):
    combinations = [[False for _ in pi] for _ in pi]
    
    for i in range(len(pi)):
        for j in range(i, len(pi)):
            if pi[i : j + 1] in numbers:
                combinations[i][j] = True
                
    cuts = [float("inf") for num in pi]
    cuts[0] = 0
    
    for i in range(1, len(pi)):
        if combinations[0][i] == True:
            cuts[i] = 0
        else:
            for j in range(0, i + 1):
                if combinations[j][i] == True:
                    cuts[i] = min(cuts[j - 1] + 1, cuts[i])

    if cuts[-1] != float("inf"):
        return cuts[-1]
    else:
        return -1

        
    
pi = "31415"
numbers = ["31", "26", "41", "5"]
print(numbersInPi(pi, numbers))
