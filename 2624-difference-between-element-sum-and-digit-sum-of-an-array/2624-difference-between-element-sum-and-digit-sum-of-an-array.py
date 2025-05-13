class Solution(object):
    def differenceOfSum(self, nums):
        def digsum(n):
            s=0
            for i in str(n):
                s+=int(i)
            return s

        s1=sum(nums)
        s2=0
        for i in nums:
            s2+=digsum(i)
        return abs(s1-s2)