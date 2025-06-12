class Solution(object):
    def maximumCount(self, nums):
       cp=0
       cn=0
       for i in nums:
        if i<0:
            cn+=1
        elif i>0:
            cp+=1
       return max(cp,cn)