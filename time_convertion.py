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
    h, m, se = s.split(':')
    se = se[:-2]
    if s.endswith('AM'):
        if h == '12':
            return '00'+':'+m+':'+se
        else:
            return h+':'+m+':'+se
    if s.endswith('PM'):
        if int(h) == 12:
            return '12'+':'+m+':'+se
        else:
            h = int(h) + 12
            return str(h)+':'+m+':'+se
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
