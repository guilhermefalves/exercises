from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = None, head
        while next is not None:
            temp = next.next
            next.next = prev
            prev = next
            next = temp
        return prev


    def print(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val)
            head = head.next

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
s = Solution()
s.print(head)
print("reversed: ")
reverse = s.reverseList(head)
s.print(reverse)