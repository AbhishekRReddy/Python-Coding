'''
https://leetcode.com/problems/contains-duplicate/description/
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                return True
            dict_nums[num] = 1
        return False