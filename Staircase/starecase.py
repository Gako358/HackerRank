#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for stairs in range(0, n + 1):
        print (("#" * stairs).rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)

