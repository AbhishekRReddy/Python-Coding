'''
https://leetcode.com/problems/concatenation-of-array/description/
'''

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l = len(nums)
        ans = [0] * (2 *l)
        for i,n in enumerate(nums):
            ans[i] = n
            ans[i+l] = n
        return ans