class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        s=0
        c=Counter(nums)
        for i in c:
            if c[i]%k==0:
                s+=i*c[i]
        return s