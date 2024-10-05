class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 1
    while counter <= k:
        second = second.next
        counter += 1
        
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return first
        
    while second.next is not None:
        second = second.next
        first = first.next
        
    first.next = first.next.next
    return head
        
