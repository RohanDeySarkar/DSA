# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	while currentNode is not None:
		nextNode = currentNode.next
		while nextNode is not None and nextNode.value == currentNode.value:
			nextNode = nextNode.next
		currentNode.next = nextNode
		currentNode = currentNode.next
	return linkedList


# alternative
def removeDuplicatesFromLinkedList(linkedList):
    seenItems = []
    head = linkedList
    while head is not None:
        if head.value not in seenItems:
            seenItems.append(head.value)
        head = head.next

    newLinkedList = LinkedList(seenItems[0])
    newNode = newLinkedList
    for i in range(1, len(seenItems)):
        newNode.next = LinkedList(seenItems[i])
        newNode = newNode.next
    return newLinkedList