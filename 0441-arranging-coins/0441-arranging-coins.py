class Solution(object):
    def arrangeCoins(self, n):
        # rc=0
        # i=1
        # while n>=0:
        #     n-=i
        #     rc+=1
        #     i+=1
        # return rc-1
        return int(((-1 + (1 + 8 * n) ** 0.5) // 2))