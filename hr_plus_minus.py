# Time Complexity: O(n)
# Space Complexity: O(1)

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

def plusMinus(arr):
    # Write your code here
    c_p = 0
    c_n = 0
    c_z = 0
    
    for i in arr:
        if i > 0:
            c_p += 1
        elif i < 0:
            c_n += 1
        else:
            c_z += 1
    
    n = len(arr)
    # Use :.6f to format the float to 6 decimal places
    print(f"{c_p / n:.6f}")
    print(f"{c_n / n:.6f}")
    print(f"{c_z / n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
