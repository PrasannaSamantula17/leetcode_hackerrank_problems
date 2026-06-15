# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = 0
        total_sum = sum(nums)
        answer = []
        
        for i in range(n):
            # The right_sum is total - left - current element
            right_sum = total_sum - left_sum - nums[i]
            
            # Calculate the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum for the next iteration
            left_sum += nums[i]
            
        return answer
