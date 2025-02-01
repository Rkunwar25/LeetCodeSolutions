class Solution(object):
    def largestAltitude(self, gain):
        current=0
        maxh=0
        for i in gain:
            current+=i
            maxh=max(maxh,current)
        return maxh