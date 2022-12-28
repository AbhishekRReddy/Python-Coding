'''
https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
def pageCount(n, p):
    # Write your code here
    pages=[]
    pages.append(1)
    if(n%2==1):
        for i in range(1,int((n-1)/2)+1):
            pages[i].append((i+1,i+2))
        
    print(pages) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
