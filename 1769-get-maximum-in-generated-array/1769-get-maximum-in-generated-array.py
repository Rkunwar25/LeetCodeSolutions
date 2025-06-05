class Solution(object):
    def getMaximumGenerated(self, n):
        if n==0:
            return 0
        l=[0]*(n+1)
        l[0],l[1]=0,1    
        for i in range(1,(n//2)+1):
            if 2*i<=n:
                l[2*i]=l[i]
            if 2*i+1<=n:
                l[2*i+1]=l[i]+l[i+1]
        return max(l)