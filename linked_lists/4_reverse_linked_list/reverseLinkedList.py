# O(n) time | O(1) space
def reverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
