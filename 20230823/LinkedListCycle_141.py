#!/usr/bin/python3

""" Easy, Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.

NOTE that the constraintes are very important !!! It shows the linked list can be empty!
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    """Runtime 76.35%, Memory 8.7%"""
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # return True or False is easy, while return 'pos' will be medium (slow/fast pointers).
        seen = {head}
        while head.next:
            if head.next in seen:
                return True
            seen.add(head.next)
            head = head.next
        return False


    """Runtime 89.44%, Memory 87.53%
    'Slow fast pointers' is a good solution handling problems on linked list cycles.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow fast two pointers.
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
