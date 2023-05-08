'''
https://www.codingninjas.com/codestudio/problems/minimum-number-of-platforms_799400?leftPanelTab=1
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    timings = [(a,1) for a in at] + [(b,-1) for b in dt]
    timings.sort(key = lambda x : x[0])
    platforms = 1
    platforms_in_use = 0
    for train in timings:
        if train[1] == 1:
            if platforms_in_use < platforms:
                platforms_in_use += 1
            else:
                platforms += 1
                platforms_in_use += 1
        else:
            platforms_in_use -= 1
    return platforms









# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)