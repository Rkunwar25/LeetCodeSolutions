class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digSum(n):
            s=0
            while n:
                s+=n%10
                n//=10
            return s
        mn=float('inf')
        for i in nums:
            mn=min(mn,digSum(i))
        return mn