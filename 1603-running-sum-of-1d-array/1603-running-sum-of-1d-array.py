class Solution(object):
    def runningSum(self, nums):
        l=[]
        l.append(nums[0])
        for i in range(1,len(nums)):
            l.append(l[i-1]+nums[i])
        return l