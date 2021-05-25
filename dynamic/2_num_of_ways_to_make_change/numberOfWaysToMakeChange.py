# Time O(len(ways)*len(arr))
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for value in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if amount >= denom:
                ways[amount] = ways[amount] + ways[amount - denom]
    return ways[n]


n = 10
denoms =[1,5,10,25]
print(numberOfWaysToMakeChange(n, denoms))
