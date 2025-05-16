class Solution(object):
    def findGCD(self, nums):
        mn=min(nums)
        mx=max(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(mx,mn)