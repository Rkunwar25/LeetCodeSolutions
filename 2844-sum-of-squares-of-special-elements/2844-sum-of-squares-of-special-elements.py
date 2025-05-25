class Solution(object):
    def sumOfSquares(self, nums):
        s=0
        n=len(nums)
        for i,j in enumerate(nums,start=1):
            if n%i==0:
                s+=(j**2)
        return s