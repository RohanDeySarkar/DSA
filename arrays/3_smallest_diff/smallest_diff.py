# O(Mlogn + Nlogn) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf") # infinity
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair

            
arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]
print(smallestDifference(arrayOne, arrayTwo))
