# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head

        if not head:
            return

        while c:
            n = c.next
            c.next = p
            p = c
            c = n
            if c:
                n = c.next

        head = p

        return head  

# TC : O(N)
# SC : O(1)