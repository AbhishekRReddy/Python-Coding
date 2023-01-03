#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    alen=len(a)
    longest=0
    for i,num in enumerate(a):
        current_length=1
        for j in range(i+1,alen):
            if(abs(num-a[j])<=1):
                current_length+=1
        if(current_length>longest):
            longest=current_length
        
    return longest
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
