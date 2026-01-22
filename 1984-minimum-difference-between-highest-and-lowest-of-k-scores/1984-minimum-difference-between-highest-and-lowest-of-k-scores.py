class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        mn = float('inf')
        
        for i in range(len(nums) - k + 1):
            mn = min(mn, nums[i + k - 1] - nums[i])
        
        return mn
