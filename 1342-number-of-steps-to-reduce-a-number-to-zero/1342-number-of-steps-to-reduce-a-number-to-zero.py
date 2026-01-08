class Solution(object):
    def numberOfSteps(self, num):
        def isZero(n):
            if n==0:
                return 0
            return n//2 if n%2==0 else n-1
        step=0
        while num!=0:
            num=isZero(num)
            step+=1
        return step