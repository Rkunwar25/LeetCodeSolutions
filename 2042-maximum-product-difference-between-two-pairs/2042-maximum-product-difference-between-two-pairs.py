class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        n=len(nums)
        return nums[n-1]*nums[n-2]-nums[1]*nums[0]