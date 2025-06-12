class Solution(object):
    def maxAdjacentDistance(self, nums):
        mx=float('-inf')
        for i in range(len(nums)-1):
            mx=max(mx,abs(nums[i]-nums[i+1]))
        mx=max(mx,abs(nums[0]-nums[len(nums)-1]))
        return mx