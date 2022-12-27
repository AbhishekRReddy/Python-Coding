'''
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_score=scores[0]
    min_score=scores[0]
    record=[0,0]
    for score in scores:
        if(score>max_score):
            max_score=score
            record[0]+=1
        elif(score<min_score):
            min_score=score
            record[1]+=1
    return record           
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
 