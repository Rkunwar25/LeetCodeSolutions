class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        sum1=l*(l+1)/2
        sum2=sum(nums)   
        return sum1-sum2