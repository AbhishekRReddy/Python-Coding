'''
https://leetcode.com/problems/single-number/description/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
#The subject solution uses the XOR bit manipulation
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor


        