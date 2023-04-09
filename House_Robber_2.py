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
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp ={}
        solA = loot(nums[:-1],len(nums)-2,dp)
        dp ={}
        solB = loot(nums[1:],len(nums)-2, dp)
        return max(solA,solB)


'''
Tabular method
'''
def loot(nums,i):
    dp =[0]*len(nums)
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        left = nums[i]
        if i > 1:
            left += dp[i-2]
        right = dp[i-1]
        dp[i] = max(left, right)
    return dp[-1]

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        solA = loot(nums[:-1],len(nums)-2)
        solB = loot(nums[1:],len(nums)-2)
        return max(solA,solB)

'''
Tabular method with Space Optimization.
'''
def loot(nums,i):
    prev1 = nums[0]
    prev2 = 0
    curri = nums[0]
    for i in range(1,len(nums)):
        left = nums[i] + prev2
        right = prev1
        curri = max(left, right)
        prev2 = prev1
        prev1 =curri
    return curri

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        solA = loot(nums[:-1],len(nums)-2)
        solB = loot(nums[1:],len(nums)-2)
        return max(solA,solB)

