'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy=100
    n=len(c)
    cloud=0
    flag=True
    while True:
        cloud=(cloud+k)%n
        if(cloud==0):
            if(c[cloud]==0):
                energy-=1
            else:
                energy-=3
            break
        elif(c[cloud]==0):
            energy-=1
        elif(c[cloud]==1):
            energy-=3
    return energy        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
