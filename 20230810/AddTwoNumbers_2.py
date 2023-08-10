#!/usr/bin/python3
""" Medium: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int = 0, next:ListNode = None):
        self.val = val
        self.next = next

class Solution:

    # Runtime 92%, Memory 92.97%. BEST solution same as mine.
    def addTwoNumbers_1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # Use `root` to remember the entrance address of the linked-list l1 because we will
        # repeatedly let `l1=l1.next`.
        # It's better assign all values one by one. This using means to make the logic clear.
        root, pre1 = l1, None
        while l1 and l2:
            """ # Use function `divmod()` to replace the following makes the code clear.
                _sum = l1.val + l2.val + carry
                l1.val = _sum % 10
                carry = _sum // 10
            """
            carry, l1.val = divmod(l1.val+l2.val+carry, 10)

            # It's very important to store the `pre-node` of the l1 before l1 becomes None. Else we
            # will miss the connection with the left nodes.
            pre1, pre2 = l1, l2
            l1, l2 = l1.next, l2.next

        if l1 is None:
            # TODO: actually we only need `pre1` because pre2.next is the current `l2`.
            pre1.next = l2
            # If this is missed, the next `while` judgement will make mistakes.
            l1 = pre1.next

        if carry == 0:
            # Necessary to early stop when l2 is much longer than l1 and carry is 0.
            return root

        while l1:
            carry, l1.val = divmod(l1.val+carry, 10)
            if carry == 0:
                # Early stop. The following numbers can keep the same.
                return root
            pre1 = l1
            l1 = l1.next
        if carry == 1:
            pre1.next = ListNode(val=1)
        return root
