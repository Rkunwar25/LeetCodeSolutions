class Solution(object):
    def subtractProductAndSum(self, n):
        s=str(n)
        p=1
        sm=0
        for i in s:
            p*=int(i)
            sm+=int(i)
        return p-sm