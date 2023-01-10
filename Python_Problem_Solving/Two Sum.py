'''
https://leetcode.com/problems/two-sum/description/
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices={}
        for i,_ in enumerate(nums):
            if(target-nums[i] in indices):
                return [indices[target-nums[i]],i]
            indices[nums[i]]=i
