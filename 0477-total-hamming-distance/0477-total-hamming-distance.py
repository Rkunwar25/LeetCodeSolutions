class Solution(object):
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        for i in range(32):  # For 32-bit integers
            bit_count = 0
            for num in nums:
                bit_count += (num >> i) & 1
            total += bit_count * (n - bit_count)
        return total