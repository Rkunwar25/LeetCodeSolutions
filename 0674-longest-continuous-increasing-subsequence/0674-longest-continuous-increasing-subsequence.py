class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx=1
        size=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                size+=1
                mx=max(mx,size)
            else:
                size=1
        return mx