'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                continue
            current_node = current_node.next
        return head
