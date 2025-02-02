class Solution(object):
    def kthFactor(self, n, k):
        fctr=[]
        x=1
        for i in range(1,n+1):
            if x==k and n%i==0:
                return i
            elif n%i==0:
                x+=1
        return -1