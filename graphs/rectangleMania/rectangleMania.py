UP = "up"
RIGHT = "right"
DOWN = "down"
LEFT = "left"

def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
	# print(coordsTable)
	return getRectangleCount(coords, coordsTable)
	
def getCoordsTable(coords): 
	coordsTable = {}
	for coord1 in coords:
		coord1Directions = {UP: [], RIGHT: [], DOWN: [], LEFT: []}
		for coord2 in coords:
			coord2Direction = getCoordDirection(coord1, coord2)
			if coord2Direction in coord1Directions:
				coord1Directions[coord2Direction].append(coord2)
		
		coord1String = coordToString(coord1)
		coordsTable[coord1String] = coord1Directions
		
	return coordsTable
		
def getCoordDirection(coord1, coord2):
	x1, y1 = coord1[0], coord1[1]
	x2, y2 = coord2[0], coord2[1]
	if x1 == x2:
		if y1 < y2:
			return UP
		elif y1 > y2:
			return DOWN
	elif y1 == y2:
		if x1 < x2:
			return RIGHT
		elif x1 > x2:
			return LEFT
	return ""

def coordToString(coord):
	x, y = coord[0], coord[1]
	return str(x) + "-" + str(y)


def getRectangleCount(coords, coordsTable):
	rectangleCount = 0
	for coord in coords:
		rectangleCount += clockWiseCount(coord, coordsTable, UP, coord)
	return rectangleCount
	
def clockWiseCount(coord, coordsTable, direction, origin):
	coordString = coordToString(coord)
	
	if direction == LEFT:
		reactangleFound = origin in coordsTable[coordString][LEFT]
		return 1 if reactangleFound else 0
	else:
		rectangleCount = 0
		nextCoords = coordsTable[coordString][direction]
		nextDirection = getNextClockwiseDirection(direction)
		for nextCoord in nextCoords:
			rectangleCount += clockWiseCount(nextCoord, coordsTable, nextDirection, origin)
		
		return rectangleCount
	
def getNextClockwiseDirection(direction):
	if direction == UP:
		return RIGHT
	if direction == RIGHT:
		return DOWN
	if direction == DOWN:
		return LEFT
	return ""
	
