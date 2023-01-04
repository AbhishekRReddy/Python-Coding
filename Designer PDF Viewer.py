'''
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
'''
#!/bin/python3
import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    alpha_map={}
    for i in range(26):
        alpha_map[chr(97+i)]=h[i]
    tallest_height=0
    for letter in word:
        if(alpha_map[letter]>tallest_height):
            tallest_height=alpha_map[letter]            
    return tallest_height*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
