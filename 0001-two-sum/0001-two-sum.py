class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if (nums[i]+nums[j]==target) and (i!=j):
                    return [i,j]
        return []