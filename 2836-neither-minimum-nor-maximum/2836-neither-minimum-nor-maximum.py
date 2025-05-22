class Solution(object):
    def findNonMinOrMax(self, nums):
        # nums.sort()
        # if nums:
        #           nums.pop(nums.index(max(nums)))
        # if nums:
        #           nums.pop(nums.index(min(nums)))
        # return nums[0] if nums else -1
        nums.sort()
        return nums[1] if (nums and len(nums)>=3) else -1