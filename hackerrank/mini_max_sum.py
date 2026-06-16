# Time Complexity - O(n)
# Space Complexity - O(1)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Calculate the total sum of all elements
    total_sum = sum(arr)
    
    # The minimum sum is total minus the maximum element
    min_sum = total_sum - max(arr)
    
    # The maximum sum is total minus the minimum element
    max_sum = total_sum - min(arr)
    
    # Print the result as two space-separated integers
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
