#!/usr/bin/python3

""" Easy: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Runtime 94.58%, Memory 18.14%"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        root = None
        while head:
            root = ListNode(head.val, root)
            head = head.next
        return root


    """From other author, decrease memory consuming"""
    def reverseList(self, head):
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node

        return new_list
