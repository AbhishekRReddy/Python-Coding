'''
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    colours={}
    pairs=0
    for a in ar:
        colours[a]=0
    for a in ar:
        if(colours[a]!=2):
            colours[a]+=1
        if(colours[a]==2):
            pairs+=1
            colours[a]=0
    return(pairs) 
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

