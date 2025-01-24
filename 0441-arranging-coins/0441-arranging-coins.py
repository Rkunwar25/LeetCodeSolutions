class Solution(object):
    def arrangeCoins(self, n):
        rc=0
        i=1
        while n>=0:
            n-=i
            rc+=1
            i+=1
        return rc-1