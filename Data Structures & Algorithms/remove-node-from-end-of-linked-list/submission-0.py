# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        storage = []

        curr = head
        while curr:
            storage.append(curr)
            curr = curr.next
        
        remove = len(storage) - n
        if remove == 0:
            return head.next
        
        storage[remove - 1].next = storage[remove].next
        return head