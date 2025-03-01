class Solution(object):
    def maximumDifference(self, nums):
        maxd=-1
        for i in range(0,len(nums)-1):
          for j in range(i+1,len(nums)) :
            if (nums[j]-nums[i])>maxd and (nums[j]-nums[i])>0:
                maxd=nums[j]-nums[i]
        return maxd