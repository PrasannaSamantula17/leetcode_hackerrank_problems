# Time Complexity - O((n+m) log n)
# Space Complexity - O(n+m)

import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 1. Sort the numbers to pick the smallest elements first
        nums.sort()
        
        # 2. Build the prefix sum array
        prefix_sum = []
        current = 0
        for x in nums:
            current += x
            prefix_sum.append(current)
            
        # 3. For each query, use binary search to find how many fit
        res = []
        for q in queries:
            # bisect_right finds the insertion point, 
            # which is equal to the count of elements <= q
            index = bisect.bisect_right(prefix_sum, q)
            res.append(index)
            
        return res
