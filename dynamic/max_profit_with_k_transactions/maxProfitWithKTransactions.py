def maxProfitWithKTransactions(prices, k):
	if not len(prices):
		return 0
    profits = [[0 for col in prices] for row in range(k + 1)]
	for row in range(1, k + 1):
		maxSoFar = float("-inf")
		for col in range(1, len(prices)):
			maxSoFar = max(maxSoFar, - prices[col - 1] + profits[row - 1][col - 1])
			profits[row][col] = max(profits[row][col - 1], prices[col] + maxSoFar)
	return profits[-1][-1]


# Make the space complexity better(since current and prev row is only in use )
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	oddProfits = [0 for price in prices]
	evenProfits = [0 for price in prices]
	for t in range(1, k + 1):
		maxSoFar = float("-inf")
		if t % 2 == 1:
			currentProfits = oddProfits
			prevProfits = evenProfits
		else:
			prevProfits = oddProfits
			currentProfits = evenProfits
		for d in range(1, len(prices)):
			maxSoFar = max(maxSoFar, - prices[d - 1] + prevProfits[d - 1])
			currentProfits[d] = max(currentProfits[d - 1], maxSoFar + prices[d])
	
	return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]

