# Time Complexity - O(n)
# Spae Complexity - O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map = {0:-1}
        prefix = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in prefix_map:
                max_len = max(max_len,i-prefix_map[prefix])
            else:
                prefix_map[prefix] = i
            
        return max_len
