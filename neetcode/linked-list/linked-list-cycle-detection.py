from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while True:
            next = head.next
            if next is not None and next.val < head.val:
                return True

            head = head.next
            if head is None:
                return False

n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n4.next = n2
n1 = ListNode(1, n2)

s = Solution()
print(s.hasCycle(n1))


head = ListNode(1, ListNode(2))
print(s.hasCycle(head))