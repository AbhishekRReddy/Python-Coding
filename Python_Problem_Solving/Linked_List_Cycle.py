
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        first_speed_node = head
        second_speed_node = head.next.next if head and head.next else None
        while first_speed_node and second_speed_node:
            if first_speed_node == second_speed_node:
                return True
            first_speed_node = first_speed_node.next
            if second_speed_node.next:
                second_speed_node = second_speed_node.next.next
            else:
                second_speed_node = None
        return False
