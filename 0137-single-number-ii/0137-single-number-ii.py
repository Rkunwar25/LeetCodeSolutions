class Solution(object):
    def singleNumber(self, nums):
    #    for i in nums:
    #     if nums.count(i)==1:
    #         return i
         c=Counter(nums)
         for i in nums:
            if c[i]==1:
                return i