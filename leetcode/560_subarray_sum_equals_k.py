# Time Complexity - O(n)
# Space Compexity - O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Map to store prefix_sum -> frequency
        # Initialize with 0:1 to handle subarrays starting from index 0
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Check if (current_sum - k) exists in the map
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            
            # Update the map with the current_sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count
