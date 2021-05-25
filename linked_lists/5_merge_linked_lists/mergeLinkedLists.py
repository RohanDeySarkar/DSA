class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p2 = headTwo
    prev = None
    
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1

    if p1 is None:
        prev.next = p2

    return headOne if headOne.value < headTwo.value else headTwo

# Recursion
def mergeLinkedLists(headOne, headTwo):
	helper(headOne, headTwo, None)
	return headOne if headOne.value < headTwo.value else headTwo

def helper(p1, p2, prev):
	if p1 is None:
		prev.next = p2
		return
	if p2 is None:
		return
	if p1.value < p2.value:
		helper(p1.next, p2, p1)
	else:
		if prev is not None:
			prev.next = p2
		newP2 = p2.next
		p2.next = p1
		helper(p1, newP2, p2)
