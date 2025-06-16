class Solution(object):
    def findMaxK(self, nums):
        val=-1
        nums.sort(reverse=True)
        for i in nums:
            if i>0 and (-1*i) in nums:
                return i
        return val