#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumArr = sum(arr)
    arrMax = max(arr)
    arrMin = min(arr)
    print (sumArr - arrMax, sumArr - arrMin)

if __name__ == '__main__':
    arr = [5,5,5,5,5]

    miniMaxSum(arr)
