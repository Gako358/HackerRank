import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    posCounter = 0
    negCounter = 0
    zeroCounter = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            posCounter += 1
        if arr[i] < 0:
            negCounter += 1
        if arr[i] == 0:
            zeroCounter += 1

    print ("%f"% (posCounter / len(arr)))
    print ("%f"% (negCounter / len(arr)))
    print ("%f"% (zeroCounter / len(arr)))

    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        plusMinus(arr)
