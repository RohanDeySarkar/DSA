def sunsetViews(buildings, direction):
	startIdx = 0 if direction == "WEST" else len(buildings) - 1
	step = 1 if direction == "WEST" else - 1
	sunsetBuildings = []
	currMaxHeight = 0
	idx = startIdx
	while idx >= 0 and idx <= len(buildings) - 1:
		if buildings[idx] > currMaxHeight:
			currMaxHeight = buildings[idx]
			sunsetBuildings.append(idx)
		idx += step
	return sunsetBuildings if direction == "WEST" else sunsetBuildings[::-1]
