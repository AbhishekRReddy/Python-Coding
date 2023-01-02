'''
https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sealevel=0
    valley=False
    No_of_valleys=0
    for step in path:
        if(sealevel<0):
            valley=True
        if(step=='U'):
            sealevel+=1
        elif(step=='D'):
            sealevel-=1
        if(valley and sealevel==0):
            No_of_valleys+=1
            valley=False
    return No_of_valleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
