class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        def harsh(n):
            s=0
            for i in str(n):
                s+=int(i)
            return s
        
        y=harsh(x)
        if x%y==0:
            return y
        else:
            return -1