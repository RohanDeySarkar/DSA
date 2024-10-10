class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 1
    while counter <= k:
        second = second.next
        counter += 1
        
    if second is None:
        first.value = first.next.value
        first.next = first.next.next
        return head
        
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
    return head
        
