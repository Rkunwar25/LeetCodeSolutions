class Solution(object):
    def countOdds(self, low, high):
        h=(high+1)//2
        l=low//2
        return h-l