'''
https://leetcode.com/problems/get-maximum-in-generated-array/description/
'''

def f(n,nums):
    if n == 0:
        nums[0] = 0
        return nums[0]
    if n == 1:
        nums[1] = 1
        return nums[1]
    if nums[n] != -1:
        return nums[n]
    if n % 2 == 0:
        nums[n] = f(n//2,nums)
        return nums[n]
    else:
        nums[n] = f(n//2,nums) + f((n//2)+1,nums)
        return nums[n]

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1] * (n+1)
        for i in range(n,-1,-1):
            f(i,nums)
        return max(nums)
    
'''
Tabulation
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1] * (n+1)
        nums[0] = 0
        if n == 0:
            return nums[0]
        nums[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[(i//2)+1]
        return max(nums)
