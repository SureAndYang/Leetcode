#!/usr/bin/python3

""" Medium: Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Runtime 66.69%, Memory 69.78%"""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(next=head)

        i, pre = 1, root
        while head.next:
            """Knowing clearly where is the 'pre' is very important"""
            if i == n:
                pre = pre.next
            else:
                i += 1
            head = head.next
        pre.next = pre.next.next
        return root.next


    """From other author, reduce memory a bit"""
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
