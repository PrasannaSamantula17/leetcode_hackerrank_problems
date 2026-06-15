class NumArray:
    def __init__(self, nums: List[int]):
        # Create an array of size n + 1 to store cumulative sums
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            # Fill the array: index i+1 holds sum of nums[0...i]
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Subtract the sum before 'left' from the sum up to 'right'
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
