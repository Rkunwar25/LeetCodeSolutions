class Solution(object):
    def reverse(self, x):
        mn,mx=-2**31,2**31-1
        s=-1 if x<0 else 1
        x=abs(x)
        n=str(x)[::-1]
        if int(n)*s<mn or int(n)*s>mx:
            return 0
        else:
            return int(n)*s