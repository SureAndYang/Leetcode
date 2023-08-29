#!/usr/bin/python3

""" Medium: Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Runtime 54.22%, Memory 81.82%"""
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = ListNode(next=head)
        lead, curr, pre = root, head, None
        while curr:
            after = curr.next
            """Combing up all logics when exchanging nodes is the core"""
            if curr.val < x:
                if pre:
                    # Need exchange.
                    lead.next, curr.next = curr, lead.next
                    pre.next = after
                lead = lead.next
            else:
                pre = curr
            curr = after
        return root.next
