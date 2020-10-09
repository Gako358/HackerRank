#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    dp = [[1], [1]]
    if x == 1:
        dp = [[1], [0]]
    else:
        dp = [[1], [1]]

    for x in range(n - 2):
        dp[0].append(dp[0][-1] * (k - 1) % (10 ** 9 + 7))
        dp[1].append((dp[0][-1] - dp[1][-1]) % (10 ** 9 + 7))
    return dp[1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
