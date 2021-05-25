def rearrangeLinkedList(head, k):
    smallerHead = None
	smallerTail = None
	equalHead = None
	equalTail = None
	greaterHead = None
	greaterTail = None
	
	node = head
	while node is not None:
		if node.value < k:
			smallerHead, smallerTail = growLinkedList(smallerHead, smallerTail, node)
		elif node.value > k:
			greaterHead, greaterTail = growLinkedList(greaterHead, greaterTail, node)
		else:
			equalHead, equalTail = growLinkedList(equalHead, equalTail, node)
			
		prev = node
		node = node.next
		prev.next = None
		
	firstHead, firstTail = connectLinkedLists(smallerHead, smallerTail, equalHead, equalTail)
	finalHead, _ = connectLinkedLists(firstHead, firstTail, greaterHead, greaterTail)
	
	return finalHead
		
		
def growLinkedList(head, tail, node):
	newHead = head
	newTail = node
	
	if newHead is None:
		newHead = node
	if tail is not None:
		tail.next = node
	
	return (newHead, newTail)

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
	newHead = headOne if headOne is not None else headTwo
	newTail = tailTwo if tailTwo is not None else tailOne
	
	if tailOne is not None:
		tailOne.next = headTwo
	
	return (newHead, newTail)



# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
