def cycleInGraph(edges):
    numberOfNodes = len(edges)
	visited = [False for _ in range(numberOfNodes)]
	nodesInStack = [False for _ in range(numberOfNodes)]
	
	for node in range(numberOfNodes):
		if visited[node]:
			continue
		hasCycle = checkCycle(node, edges, visited, nodesInStack)
		if hasCycle:
			return True
	return False

def checkCycle(node, edges, visited, nodesInStack):
	visited[node] = True
	nodesInStack[node] = True
	
	neighbors = edges[node]
	
	for neighbor in neighbors:
		if not visited[neighbor]:
			hasCycle = checkCycle(neighbor, edges, visited, nodesInStack)
			if hasCycle:
				return True
		if nodesInStack[neighbor]:
			return True
	nodesInStack[node] = False
	return False
