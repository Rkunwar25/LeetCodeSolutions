class Solution(object):
    def smallestRangeI(self, nums, k):
        if len(nums) == 1:
          return 0
    
    # Calculate the minimum and maximum of the array
        max_num = max(nums)
        min_num = min(nums)
    
       # Calculate the minimum possible score after the operation
        return max(0, (max_num - k) - (min_num + k))