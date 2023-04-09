'''
https://www.codingninjas.com/codestudio/problems/loot-houses_630510?leftPanelTab=1

'''

from sys import stdin

def loot(houses, n, dp):
    if n == 0:
        return houses[0]
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = houses[n]+ loot(houses,n-2,dp)
    right = loot(houses,n-1,dp)
    dp[n] = max(left,right)
    return dp[n]

def maxMoneyLooted(houses, n) :
    #Your code goes here
    dp = [0]*n
    prev1 = houses[0]
    prev2 = 0
    curri = houses[0]
    for i in range(1,n):
        left = houses[i] + prev2
        right = prev1
        curri = max(left,right)
        prev2 = prev1
        prev1 = curri
    return curri

#taking input using fast I/O method

def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
print(maxMoneyLooted(arr, n))