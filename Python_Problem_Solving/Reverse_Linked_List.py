'''
https://leetcode.com/problems/reverse-linked-list/description/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
            

