# Time Compexity - O(1)
# Space Compleixty - O(1)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    # XOR the bounds to find the most significant bit that differs
    xor_val = l ^ r
    
    # Find the position of the highest set bit
    # This represents the power of 2 that covers the difference
    bit_length = xor_val.bit_length()
    
    # The maximum XOR will be a sequence of 1s equal to the bit length
    # (2^bit_length) - 1 creates a number with all 1s of that length
    return (1 << bit_length) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
