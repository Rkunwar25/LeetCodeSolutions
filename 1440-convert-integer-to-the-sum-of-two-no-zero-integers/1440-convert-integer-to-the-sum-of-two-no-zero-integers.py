class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n//2+1):
            if ('0' not in str(i)) and ('0' not in str(n-i)):
                return [i,n-i]