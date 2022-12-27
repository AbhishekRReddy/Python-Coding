#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#
def bonAppetit(bill, k, b):
    # Write your code here
    anna_ate=bill[:]
    anna_ate.pop(k)
    total_money=0
    for i in anna_ate:
        total_money+=i  
    anna_share=total_money/2
    if(anna_share==b):
        print('Bon Appetit')
    else:
        print(int(b-anna_share))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
