class Solution(object):
    def targetIndices(self, nums, target):
       l=[]
       nums.sort()
       for i in range(len(nums)):
        if nums[i]==target:
            l.append(i)
       return l