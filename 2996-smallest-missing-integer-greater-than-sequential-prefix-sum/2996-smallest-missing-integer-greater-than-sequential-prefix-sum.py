class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=nums[0]
        i=1
        n=len(nums)
        while i<n and nums[i]==nums[i-1]+1:
            s+=nums[i]
            i+=1
        while s in nums:
            s+=1
        return s