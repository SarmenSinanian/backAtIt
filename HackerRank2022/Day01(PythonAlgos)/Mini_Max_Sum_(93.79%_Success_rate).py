#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mini = 0
    maxi = 0
    arr.sort()
    for i in range(4):
        mini += arr[i]
    for i in range(1,5):
        maxi += arr[i]
    print(mini, maxi)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
 
