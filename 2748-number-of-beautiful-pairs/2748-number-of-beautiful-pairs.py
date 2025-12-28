class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    count+=1
        return count