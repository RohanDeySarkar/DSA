def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)
    
def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        matchIdx = string.find(substring, startIdx)
        if matchIdx != -1:
            locations.append([matchIdx, matchIdx + len(substring)])
            startIdx = matchIdx + 1
        else:
            break
##    print(locations)
    return locations

def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
##            print(newLocations)
        else:
            newLocations.append(current)
            previous = current
##            print(newLocations)
    return newLocations

def underscorify(string, locations):
    if not len(locations):
        return string
    finalString = []
    locationsIdx = 0
    stringIdx = 0
    i = 0
    while stringIdx < len(string):
        if stringIdx == locations[locationsIdx][i]:
            finalString.append("_")
            if i == 0:
                i = 1
            elif i == 1:
                i = 0
                if locationsIdx != len(locations) - 1:
                    locationsIdx += 1
        finalString.append(string[stringIdx])
        stringIdx += 1
    if locations[locationsIdx][i] == len(string):
        finalString.append("_")
    return "".join(finalString)
    
    
                 
string = "testthis is a testtest to see if testestest works"
substring = "test"
##string = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
##substring = "abc"
print(underscorifySubstring(string, substring))


