class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        if n==0:
            return 0
        minp=float('inf')
        maxp=0
        for i in prices:
            minp=min(minp,i)
            maxp=max(maxp,i-minp)
        return maxp