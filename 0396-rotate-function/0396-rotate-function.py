class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        max_value = F

        for k in range(1, n):
            # F(k) = F(k-1) + total_sum - n * nums[n - k]
            F = F + total_sum - n * nums[-k]
            max_value = max(max_value, F)
        
        return max_value
