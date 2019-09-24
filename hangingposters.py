#!/bin/python3
# hackerrank

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

def solve(h, wallPoints, lengths):
    if not h or not wallPoints or not lengths:
        return 0
    if len(wallPoints) != len(lengths):
        return 0

    max_height = 0;
    for i, wallPoint in enumerate(wallPoints):
        mid = wallPoint - lengths[i]//4
        max_height = max(max_height, mid)

    max_ladder = math.ceil(max_height - h)
    if max_ladder < 0:
        return 0
    else:
        return max_ladder
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    fptr.write(str(answer) + '\n')

    fptr.close()
