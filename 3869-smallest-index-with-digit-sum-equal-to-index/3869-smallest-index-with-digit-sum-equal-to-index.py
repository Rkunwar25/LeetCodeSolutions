class Solution(object):
    def smallestIndex(self, nums):
        s=-1
        for i in range(len(nums)):
            if i==sum(map(int,list(str(nums[i])))):
                s=i
                break
        return s