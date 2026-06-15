# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        res = []
        for i in nums:
            s += i
            res.append(s)
        return res
