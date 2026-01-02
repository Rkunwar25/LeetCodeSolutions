# class Solution:
#     def divideArray(self, nums: List[int]) -> bool:
#         nset=set(nums)
#         for i in nset:
#             if nums.count(i)%2!=0:
#                 return False
#         return True
from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for v in freq.values():
            if v % 2 != 0:
                return False
        return True
