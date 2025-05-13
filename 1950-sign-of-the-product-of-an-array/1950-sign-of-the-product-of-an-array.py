class Solution(object):
    def arraySign(self, nums):
        s=1
        for i in nums:
            s*=i
        if s>0:
            return 1
        elif s<0:
            return -1
        else:
            return 0        