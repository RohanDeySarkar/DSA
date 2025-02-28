def smallestSubstringContaining(bigString, smallString):
    combinations = []
    
    for i in range(len(bigString)):
        for j in range(i, len(bigString)):
            if len(bigString[i : j]) >= len(smallString) - 1:
                combinations.append(bigString[i : j + 1])
                
    length = float("inf")
    subString = None
    
    smallString = sorted(smallString)
    
    for combination in combinations:
        idx = 0
        currCombination = sorted(combination)
        
        for letter in currCombination:
            if letter == smallString[idx]:
                idx += 1
            if idx == len(smallString):
                break

        if idx == len(smallString):
            if len(combination) < length:
                length = len(combination)
                subString = combination
            
        idx = 0

    return subString if subString is not None else ""