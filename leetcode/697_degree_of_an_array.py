# Time Complexity - O(N)
# Space Complexity - O(N)

from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Frequency counter, and trackers for first/last occurrences
        count = {}
        first = {}
        last = {}
        
        # Populate the frequency counter and index trackers
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        # The degree is the maximum frequency
        degree = max(count.values())
        min_length = len(nums)
        
        # Iterate through the frequency counter
        for num in count:
            if count[num] == degree:
                # Calculate the length of the subarray
                current_length = last[num] - first[num] + 1
                # Update min_length if this is smaller
                min_length = min(min_length, current_length)
                
        return min_length
