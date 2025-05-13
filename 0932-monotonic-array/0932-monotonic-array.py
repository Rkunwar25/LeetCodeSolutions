class Solution(object):
    def isMonotonic(self, nums):
        # if sorted(nums)==nums:
        #     return True
        # elif sorted(nums,reverse=True)==nums:
        #     return True
        # else:
        #     return False
        return all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or  all(nums[i] >= nums[i+1] for i in range(len(nums) - 1))
