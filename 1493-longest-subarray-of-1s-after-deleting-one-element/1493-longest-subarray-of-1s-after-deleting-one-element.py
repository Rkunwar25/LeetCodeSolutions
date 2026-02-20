class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        nums=''.join(map(str,nums))
        nums=nums.split('0')
        mx=float('-inf')
        for i in range(1,len(nums)):
            mx=max(mx,len(nums[i])+len(nums[i-1]))
        return mx