'''
https://leetcode.com/problems/move-zeroes/description/
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        no_z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
                continue
            no_z += 1
        for i in range(len(nums)-no_z,len(nums)):
            nums[i] = 0