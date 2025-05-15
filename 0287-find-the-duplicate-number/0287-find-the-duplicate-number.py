class Solution(object):
    def findDuplicate(self, nums):
        c=Counter(nums)
        for i,j in c.items():
            if j>=2:
                return i