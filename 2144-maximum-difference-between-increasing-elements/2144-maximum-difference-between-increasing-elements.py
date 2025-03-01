# class Solution(object):
#     def maximumDifference(self, nums):
#         maxd=-1
#         for i in range(0,len(nums)-1):
#           for j in range(i+1,len(nums)) :
#             if (nums[j]-nums[i])>maxd and (nums[j]-nums[i])>0:
#                 maxd=nums[j]-nums[i]
#         return maxd
class Solution(object):
    def maximumDifference(self, nums):
        min_val = nums[0]
        maxd = -1
        
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                maxd = max(maxd, nums[i] - min_val)
            else:
                min_val = nums[i]  # Update min_val when a new smaller element is found
        
        return maxd