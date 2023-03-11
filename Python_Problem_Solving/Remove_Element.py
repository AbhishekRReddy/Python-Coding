'''
https://leetcode.com/problems/remove-element/description/
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i,elem in enumerate(nums):
            if elem == val:
                continue
            nums[k] = elem
            k += 1
        return k