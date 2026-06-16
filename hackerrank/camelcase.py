# Time Complexity - O(n)
# Space Complexity - O(1)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Initialize count to 1 for the first lowercase word
    # If the string is empty, you might return 0
    if not s:
        return 0
    
    count = 1
    # Iterate through the string and count uppercase letters
    for char in s:
        if char.isupper():
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
