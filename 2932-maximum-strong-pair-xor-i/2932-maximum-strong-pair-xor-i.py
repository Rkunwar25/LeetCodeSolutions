class Solution:
    def maximumStrongPairXor(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                if nums[j] > 2 * nums[i]:
                    break
                ans = max(ans, nums[i] ^ nums[j])

        return ans