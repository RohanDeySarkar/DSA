def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
	# check all reachable/unreachable airports from startAirport
	unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
	# create a list of airports reachable from a particular airport
	markUnreachableConnections(airportGraph, unreachableAirportNodes)
	
	return getMinNumOfNewConnections(airportGraph, unreachableAirportNodes)
	
def createAirportGraph(airports, routes):
	airportGraph = {}
	
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	
	for route in routes:
		airport, connection = route[0], route[1]
		airportGraph[airport].connections.append(connection)
		
	return airportGraph

		
class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []
		
		
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
	visitedAirports = {}
	depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
	
	# unreachable airports from startingAirport
	unreachableAirportNodes = []
	
	for airport in airports:
		if airport in visitedAirports:
			continue
		airportNode = airportGraph[airport]
		airportNode.isReachable = False
		unreachableAirportNodes.append(airportNode)
		
	return unreachableAirportNodes
	
	
def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstTraverseAirports(airportGraph, connection, visitedAirports)

	
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {})
		airportNode.unreachableConnections = unreachableConnections
	

def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
	# check if curr airport is startingAirport
	if airportGraph[airport].isReachable:
		return
	# check for loop
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	unreachableConnections.append(airport)
	connections = airportGraph[airport].connections
	for connection in connections:
		 depthFirstAddUnreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)
	
	
def getMinNumOfNewConnections(airportGraph, unreachableAirportNodes):
	unreachableAirportNodes.sort(key = lambda airport: len(airport.unreachableConnections), reverse=True)
	
	numOfNewConnections = 0
	
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numOfNewConnections += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	
	return numOfNewConnections



airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]
startingAirport = "LGA"




    
