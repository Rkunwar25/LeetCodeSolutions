# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         n=len(nums)//2
#         for i in nums:
#             if nums.count(i)==n:
#                 return i
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
