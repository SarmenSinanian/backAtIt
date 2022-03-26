#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_counter = 0
    right_counter = len(arr)-1
    left_diag = []
    right_diag = []
    for i in arr:
        left_diag.append(i[left_counter])
        left_counter+=1
    for i in arr:
        right_diag.append(i[right_counter])
        right_counter-=1
    sum_left_diag = sum(left_diag)
    sum_right_diag = sum(right_diag)
    absolute_difference = abs(sum_left_diag-sum_right_diag)
    return absolute_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
