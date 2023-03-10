# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1,list2):
        pointer = ListNode()
        result_linked_list_head = pointer
        current_node1 = list1
        print(list1)
        current_node2 = list2
        while current_node1 or current_node2:
            if current_node1 is None:
                pointer.next = current_node2
                break
            if current_node2 is None:
                pointer.next = current_node1
                break
            if current_node1.val <= current_node2.val:
                pointer.next = current_node1
                current_node1 = current_node1.next
                pointer = pointer.next
            else:
                pointer.next = current_node2
                current_node2 = current_node2.next
                pointer = pointer.next
        return result_linked_list_head.next

                



