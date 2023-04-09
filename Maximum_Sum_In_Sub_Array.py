

'''
https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def max_sum(nums,index,dp):
    if index == 0:
        return nums[0]
    if index < 0:
        return 0
    if index in dp:
        return dp[index]
    left = nums[index] + max_sum(nums,index-2,dp)
    right = 0 + max_sum(nums,index -1,dp)
    dp[index] = max(left,right)
    return dp[index]

def maximumNonAdjacentSum(nums): 
    dp = {}   
    return max_sum(nums,len(nums)-1,dp)

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1