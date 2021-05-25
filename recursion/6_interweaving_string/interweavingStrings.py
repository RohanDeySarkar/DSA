def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
	
    return areInterwoven(one, two, three, 0, 0)

def areInterwoven(one, two, three, i, j):
	k = i + j
	
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if areInterwoven(one, two, three, i + 1, j):
			return True
	
	if j < len(two) and two[j] == three[k]:
		if areInterwoven(one, two, three, i, j + 1):
			return True
	
	return False



one = "algoexpert"
two = "your-algodream-expertjob"
three = "your-dream-job"
print(interweavingStrings(one, two, three))
