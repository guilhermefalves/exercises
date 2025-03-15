from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # aux, prev = head, None
        # while n > 0 and aux is not None:
        #     prev, aux, n = aux, aux.next or None, n - 1

        # if aux is None:
        #     return head.next

        # prev.next = aux.next
        # return head

        aux, prev = head, None
        while n > 0:
            aux, n = aux.next, n - 1

        while aux:
            # prev, aux, fast = aux, aux.next, fast.next
            prev = aux
            aux = aux.next

        if aux is None:
            return head.next

        prev.next = aux.next
        return head




    def print(self, head: Optional[ListNode]) -> str:
        p = []
        while head is not None:
            p.append(str(head.val))
            head = head.next

        return ",".join(p)

s = Solution()
inputs = [
    # [ListNode(5), 1, []],
    # [ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2, [1,2,4]],
    # [ListNode(1, ListNode(2)), 2, [2]],
    # [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 6, [2,3,4,5,6]],
    [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, [1,2,3,5]],
]

for head, n, expected in inputs:
    r = s.removeNthFromEnd(head, n)
    print("List:: [{}] N:: {} Removed:: [{}] Expected {}".format(s.print(head), n, s.print(r), expected))

