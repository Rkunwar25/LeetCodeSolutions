# class Solution(object):
#     def findFinalValue(self, nums, original):
#         def prod(nums,targ):
#            for i in nums:
#               if i==targ:
#                 i=i*2
#                 break
#            return i     
        
#         while True:
#             if original in nums:
#                 original=prod(nums,original)
#             else:
#                 break          
#         return original
class Solution(object):
    def findFinalValue(self, nums, original):
        num_set = set(nums)  # O(1) lookups
        while original in num_set:
            original *= 2
        return original
