#!/usr/bin/python3

""" Easy, Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of
the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Runtime 51.92% O(n), Memory 97.83% O(1)"""
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        head, pre, rest = list1, None, list2
        while list1 and list2:
            if list1.val > list2.val:
                # Insert the current list2-node into list1, and list2 goes one step further.
                rest, list2.next = list2.next, list1
                pre.next = list2
                pre, list2 = list2, rest
            else:
                pre = list1
                list1 = list1.next
        if rest:
            pre.next = rest
        return head


    """From other author, the solution makes it clear"""
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
