from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        begin = merged = ListNode()
        while True:
            if list1 is None and list2 is None: break

            if list1 is None or (list2 is not None and list2.val <= list1.val):
                merged.next = list2
                merged = merged.next
                list2 = list2.next
                continue

            merged.next = list1
            merged = merged.next
            list1 = list1.next

        return begin.next

    def print(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val)
            head = head.next

s = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(5)))

print("List1: ")
s.print(list1)
print("List2: ")
s.print(list2)
print("Merged: ")
merged = s.mergeTwoLists(list1, list2)
s.print(merged)


list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
print("List1: ")
s.print(list1)
print("List2: ")
s.print(list2)
print("Merged: ")
merged = s.mergeTwoLists(list1, list2)
s.print(merged)

