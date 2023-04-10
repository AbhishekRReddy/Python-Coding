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



    
