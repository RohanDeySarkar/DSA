# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Recursion
def linkedListPalindrome(head):
    isEqual, _ = isPalindrome(head, head)
	return isEqual

def isPalindrome(leftNode, rightNode):
	if rightNode is None:
		return (True, leftNode)
	
	nodesAreEqual, leftNodeToCompare = isPalindrome(leftNode, rightNode.next)
	
	isEqual = nodesAreEqual and leftNodeToCompare.value == rightNode.value
	return (isEqual, leftNodeToCompare.next)


# Reverse linkedList check
def linkedListPalindrome(head):
	reverseListHead = reverseLinkedList(head)
	while head is not None and reverseListHead is not None:
		if head.value != reverseListHead.value:
			return False
		head = head.next
		reverseListHead = reverseListHead.next
	return True
	
def reverseLinkedList(head):
	prev = None
	while head is not None:
		temp = head.next
		head.next = prev
		prev = head
		head = temp
	return prev