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

######################################################################################################################
#                                                                                                                    #
#   PROBLEM LINK: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true                         #
#                                                                                                                    #
######################################################################################################################

def plusMinus(arr):
    pc = 0 #positive count
    nc = 0 #negative count
    zc = 0 #zero count
    for i in arr:
        if i > 0:
            pc += 1
        elif i < 0:
            nc += 1
        else:
            zc += 1

    ln = len(arr) #ln length of arr
          
    print("%.6f"%(pc/ln))
    print("%.6f"%(nc/ln))
    print("%.6f"%(zc/ln))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
