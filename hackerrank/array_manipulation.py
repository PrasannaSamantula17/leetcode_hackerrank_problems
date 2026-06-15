# Time Complexity: O(n + q)
# Space Complexity: O(n)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Initialize a difference array of size n+2 (1-indexed safety)
    arr = [0] * (n + 2)
    
    # Apply difference array updates
    for a, b, k in queries:
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k
            
    # Calculate prefix sums and find the maximum
    max_val = 0
    current_sum = 0
    for i in range(1, n + 1):
        current_sum += arr[i]
        if current_sum > max_val:
            max_val = current_sum
            
    return max_val
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
