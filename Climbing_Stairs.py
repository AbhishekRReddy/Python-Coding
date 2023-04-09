'''
https://leetcode.com/problems/climbing-stairs/description/
Memoization 
'''
def stairs(n,dp):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in dp:
        return dp[n] 
    left = stairs(n-1,dp)
    right = stairs(n-2,dp)
    dp[n] = left + right
    return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return stairs(n,dp)