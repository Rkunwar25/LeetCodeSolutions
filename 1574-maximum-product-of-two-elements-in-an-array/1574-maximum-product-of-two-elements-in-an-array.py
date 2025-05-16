class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        if len(nums)>=2:
            return (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)