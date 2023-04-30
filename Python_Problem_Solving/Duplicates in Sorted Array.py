'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pos = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            nums[pos] = nums[i]
            pos+=1
        return pos
        