'''
https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_800284?leftPanelTab=0
'''

def rod(price, n, index,dp):
    if n < 0:
        return float('-inf')
    if index == 0:
        cost = n * price[0]
        return cost
    if dp[n][index] != -1:
        return dp[n][index]
    left = float('-inf')
    if n >= index+1:
        left = price[index] + rod(price,n-index-1,index,dp)
    right = rod(price,n,index-1,dp)
    dp[n][index] = max(left,right)
    return dp[n][index]

a    dp = [ [-1]*(n) for _ in range(n+1)]
    return rod(price,n,n-1,dp)
    # Write your code here.













# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n
# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
'''
https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_800284?leftPanelTab=0
