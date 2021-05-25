# O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers

def numbersInPi(pi, numbers):
    minSpaces = getMinSpaces(pi, numbers, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbers, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        if prefix in numbers:
            minSpacesInSuffix = getMinSpaces(pi, numbers, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]
    
pi = "31415"
numbers = ["31", "26", "41", "5"]
print(numbersInPi(pi, numbers))
