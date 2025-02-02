class Solution(object):
    def kthFactor(self, n, k):
        fctr=[]
        for i in range(1,n+1):
            if n%i==0:
                fctr.append(i)
        fctr.sort()
        return fctr[k-1] if len(fctr)>=k else -1