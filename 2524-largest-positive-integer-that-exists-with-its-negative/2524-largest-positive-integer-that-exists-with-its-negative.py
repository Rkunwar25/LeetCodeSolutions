class Solution(object):
    def findMaxK(self, nums):
        mx=float('-inf')
        for i in nums:
            if i>0 and (-1*i) in nums:
                mx=max(mx,i)
        return mx if mx!=float('-inf') else -1