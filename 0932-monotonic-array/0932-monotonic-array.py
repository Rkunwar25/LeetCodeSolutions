class Solution(object):
    def isMonotonic(self, nums):
        if sorted(nums)==nums:
            return True
        elif sorted(nums,reverse=True)==nums:
            return True
        else:
            return False