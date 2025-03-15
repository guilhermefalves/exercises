from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next

        second = self.reverseList(slow.next)
        slow.next = None

        while second is not None:
            t1, t2 = head.next, second.next
            head.next = second
            second.next = t1
            head, second = t1, t2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = None, head
        while next is not None:
            node = ListNode(next.val)
            node.next = prev
            prev = node
            next = next.next
        return prev

    def print(self, head: Optional[ListNode]) -> str:
        p = []
        while head is not None:
            p.append(str(head.val))
            head = head.next

        return ",".join(p)

s = Solution()
inputs = [
    [ListNode(2, ListNode(4, ListNode(6, ListNode(8)))), [2,8,4,6]],
    [ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10))))), [2,10,4,8,6]]
]

for head, expected in inputs:
    aux = head
    s.reorderList(head)
    print("List:: [{}] Reordered:: [{}] Expected {}".format(s.print(aux), s.print(head), expected))
