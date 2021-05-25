def knapsackProblem(items, capacity):
    knapsackValues = [[0 for col in range(0, capacity + 1)]for row in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentValue = items[i - 1][0]
        currentWeight = items[i - 1][1]
        for col in range(0, capacity + 1):
            if col >= currentWeight:
                knapsackValues[i][col] = max(
                                            knapsackValues[i - 1][col - currentWeight] + currentValue,
                                            knapsackValues[i - 1][col]
                                            )
            else:
                knapsackValues[i][col] = knapsackValues[i - 1][col]

    knapsackItems = getKnapsackItems(knapsackValues, items)
    
    return [knapsackValues[-1][-1], knapsackItems]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    row = len(knapsackValues) - 1
    col = len(knapsackValues[0]) - 1

    while row > 0:
        if knapsackValues[row][col] == knapsackValues[row - 1][col]:
            row -= 1
        else:
            sequence.append(row - 1)
            col -= items[row - 1][1]
            row -= 1
        if col == 0:
            break
            
    return list(reversed(sequence))


	
items=[[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
print(knapsackProblem(items, capacity))