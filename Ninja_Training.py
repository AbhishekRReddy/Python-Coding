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
            score = points[n][i] + func(n-1 ,points,i,dp)
            maxP = max(maxP, score)
    if pday < 3:
        dp[n][pday] = maxP
        return dp[n][pday]
    return maxP    

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [ [-1]*3 for i in range(n)]
    return func(n-1, points,3,dp)

'''
DP With Tabulation method
'''
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # Write your code here.
    dp = [ [-1]*4 for i in range(n)] #dp[day][prev]
    #We need to write the base cases for all the day 0 for all the prev
    #conditions
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][1], points[0][0])
    dp[0][3] = max(points[0][1], max(points[0][2], points[0][0]))
    for day in range(1,n):
        for prev in range(4):
            maxi = 0
            for i in range(3):
                if i != prev:
                    point = points[day][i] + dp[day-1][i]
                    maxi = max(maxi,point)
            dp[day][prev] = maxi
    return dp[n-1][3]


    


    
