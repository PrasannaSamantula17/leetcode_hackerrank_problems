# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            # Check if number of digits is even
            # Using log10: floor(log10(num)) + 1 gives the number of digits
            if int(math.log10(num)) % 2 == 1:
                count += 1
        return count
