def longest(seq):
    maxCount = 0
    maxChar = 0
    prevChar = seq[0]
    count = 0
    for i in range(1, len(seq)):
        currentChar = seq[i]
        if currentChar == prevChar:
            count += 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count
            maxChar = currentChar
        prevChar = currentChar
        
    return {maxChar: maxCount}


seq = "AABCDDBBBEA"
print(longest(seq))
