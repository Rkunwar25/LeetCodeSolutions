class Solution(object):
    def smallestNumber(self, n, t):
        def digProd(n):
            p=1
            for i in str(n):
                p*=int(i)
            return p
        d=n
        while True:
            if digProd(d)%t==0:
                return d
            d+=1