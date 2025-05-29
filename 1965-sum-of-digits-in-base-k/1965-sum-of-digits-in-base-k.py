class Solution(object):
    def sumBase(self, n, k):
        if n==0:
            return 0
        digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res=""
        while n>0:
            res=digits[n%k]+res
            n//=k
        s=0
        for i in res:
            s+=int(i)
        return s