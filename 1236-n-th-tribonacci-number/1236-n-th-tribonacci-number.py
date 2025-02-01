class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            t0=0
            t1=1
            t2=1
            for i in range(3,n+1):
                t=t0+t1+t2
                t0,t1,t2=t1,t2,t
            return t
