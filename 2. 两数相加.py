# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else None) + (l2.val if l2 else None)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
