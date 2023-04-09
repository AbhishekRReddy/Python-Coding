'''
https://leetcode.com/problems/house-robber-ii/description/
'''
def loot(nums,i,dp):
    if i == 0:
        return nums[0]
    if i < 0:
        return 0
    if i in dp:
        return dp[i]
    left = nums[i] + loot(nums,i-2,dp)
    right = loot(nums,i-1,dp)
    dp[i] = max(left,right)
    return dp[i]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp ={}
        solA = loot(nums[:-1],len(nums)-2,dp)
        dp ={}
        solB = loot(nums[1:],len(nums)-2, dp)
        return max(solA,solB)