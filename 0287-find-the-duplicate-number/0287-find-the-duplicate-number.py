class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        duplicates = set()
        for item in nums:
           if item in seen:
             duplicates.add(item)
           else: 
             seen.add(item)
        return list(duplicates)[0]