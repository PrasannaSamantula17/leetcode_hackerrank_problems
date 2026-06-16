# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            # Calculate right sum based on total and current left_sum
            right_sum = total_sum - left_sum - val
            
            if left_sum == right_sum:
                return i
            
            # Update left_sum for the next iteration
            left_sum += val
            
        return -1
