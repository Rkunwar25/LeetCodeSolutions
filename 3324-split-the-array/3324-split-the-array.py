class Solution(object):
    def isPossibleToSplit(self, nums):
        if len(nums)%2!=0:
            return False
        c=Counter(nums)
        for i in nums:
            if c[i]>2:
                return False
        return True