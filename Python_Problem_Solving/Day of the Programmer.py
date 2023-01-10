'''
https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    day=0
    if(year<1918):
        if(year%4==0):
            day=256-(31*5+30*2+29)
        else:
            day=256-(31*5+30*2+28)
        return f'{day}.09.{year}'
    elif(year==1918):
        day=256-(31*5+30*2+15)
        return f'{day}.09.{year}'
    else:
        if(year%400==0 or (year%4==0 and year%100!=0)):
            day=256-(31*5+30*2+29)
        else:
            day=256-(31*5+30*2+28)
        return f'{day}.09.{year}'
                          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
