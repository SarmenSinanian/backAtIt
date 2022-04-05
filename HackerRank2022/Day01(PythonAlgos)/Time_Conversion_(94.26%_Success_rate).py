#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if 'PM' in s:
        if int(s[0:2]) == 12:
            return s[0:8]
        else:
            item = s[0:2]
            converted = int(item)
            converted += 12
            reconverted = str(converted)
            replacement = s.replace(s[0:2], reconverted)
            return replacement[0:8]
    if 'PM' not in s:
        if int(s[0:2]) == 12:
            item = s.replace(s[0:2], '00')
            return item[0:8]
        else:
            return s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
