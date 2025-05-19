class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        nums.sort()
        mn=float('-inf')
        for i in range(len(nums)-1):
            mn=max(mn,nums[i+1]-nums[i])
        return mn