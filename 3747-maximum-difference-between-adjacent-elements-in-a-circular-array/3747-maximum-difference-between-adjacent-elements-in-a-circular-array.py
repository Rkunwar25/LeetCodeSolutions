class Solution(object):
    def maxAdjacentDistance(self, nums):
        mx=abs(nums[0]-nums[-1])
        for i in range(len(nums)-1):
            mx=max(mx,abs(nums[i]-nums[i+1]))
        return mx