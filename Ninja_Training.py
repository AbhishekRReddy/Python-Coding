'''
https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003
'''

from typing import *

def func(n,points,pday):
    if n == 0:
        maxP = 0
        for i in range(3):
            if i != pday:
                maxP = max(maxP, points[n][i])
        return maxP
    maxP = 0 
    for i in range(3):
        if i != pday:
            score = points[n][i] + func(n-1,points,i)
            maxP = max(maxP, score)
    return maxP    

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    return func(n-1, points,3)

'''
DP- Memoization
'''
from typing import *

def func(n,points,pday,dp):
    if n == 0:
        maxP = 0
        for i in range(3):
            if i != pday:
                maxP = max(maxP, points[n][i])
        return maxP
    maxP = 0
    if pday < 3: 
        if dp[n][pday] != -1:
            return dp[n][pday]
    for i in range(3):
        if i != pday:
            score = points[n][i] + func(n-1,points,i,dp)
            maxP = max(maxP, score)
    if pday < 3:
        dp[n][pday] = maxP
        return dp[n][pday]
    return maxP    

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [ [-1]*3 for i in range(n)]
    return func(n-1, points,3,dp)



    


    
