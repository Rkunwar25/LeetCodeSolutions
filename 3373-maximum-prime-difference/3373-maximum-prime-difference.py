class Solution(object):
    def maximumPrimeDifference(self, nums):
        def isPrime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        
        l=[]
        for i in range(len(nums)):
            if isPrime(nums[i]):
                l.append(i)
        return max(l)-min(l)