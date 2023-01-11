'''
https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    n_list=[]
    m=n
    divisor=0
    while(m>0):
        digit=m%10
        n_list.append(digit)
        m=m//10
    for digit in n_list:
        if(digit==0):
            continue
        elif n%digit==0:
            divisor+=1
    return divisor
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

