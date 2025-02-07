class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for i in nums:
            l.append(i**2)
        l.sort()
        return l