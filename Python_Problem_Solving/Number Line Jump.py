'''
https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for _ in range(min(x1,x2),10001):
        if(x1==10000 or x2==10000):
            break
        x1+=v1
        x2+=v2
        if(x1==x2):
            return 'YES'
            break    
    
    return 'NO'
            
        
        

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
