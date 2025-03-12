class Solution(object):
    def smallestEqual(self, nums):
       R=-1
       for i in range(len(nums)):
        if i%10==nums[i]:
            return i
       return R