# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
	newLinkedList = LinkedList(0)
	currentNode = newLinkedList
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	carry = 0
	while nodeOne is not None or nodeTwo is not None or carry != 0:
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		
		sumOfValues = valueOne + valueTwo + carry
		# val of each node must be bet 0 - 9, so (sumOfValues % 10)
		newValue = sumOfValues % 10
		carry = sumOfValues // 10
		
		currentNode.next = LinkedList(newValue)
		currentNode = currentNode.next
		
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
		
	return newLinkedList.next
