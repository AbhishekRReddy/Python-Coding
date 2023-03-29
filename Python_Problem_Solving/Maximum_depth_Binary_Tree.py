'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(root,depth):
            if root is None:
                return depth
            left_height = max_depth(root.left,depth)
            right_height = max_depth(root.right, depth)
            return max(left_height, right_height) + 1
        return max_depth(root,0)