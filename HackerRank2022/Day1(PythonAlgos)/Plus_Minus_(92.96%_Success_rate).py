#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for i in arr:
        if i > 0:
            pos+=1
        if i < 0:
            neg+=1
        if i == 0:
            zero+=1
    pos_ratio = pos/total
    neg_ratio = neg/total
    zero_ratio = zero/total
    print(f'{pos_ratio}\n{neg_ratio}\n{zero_ratio}')
            
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
