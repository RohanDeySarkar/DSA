def minNumberOfCoinsForChange(n, denoms):
	minCoins = [float("inf") for amount in range(n + 1)]
	minCoins[0] = 0
	for denom in denoms:
		for amount in range(n + 1):
			if amount >= denom:
				minCoins[amount] = min(minCoins[amount], minCoins[amount - denom] + 1)         
	return minCoins[n] if minCoins[n] != float("inf") else -1


def minNumberOfCoinsForChange(n, denoms):
    minCoins = [float("inf") for amount in range(n + 1)]
	minCoins[0] = 0
	for i in range(1, n + 1):
		for denom in denoms:
			if i >= denom :
				minCoins[i] = min(minCoins[i], minCoins[i - denom] + 1)
	return minCoins[n] if minCoins[n] != float("inf") else -1



n = 6
denoms = [1,2,4]
print(minNumberOfCoinsForChange(n, denoms))
