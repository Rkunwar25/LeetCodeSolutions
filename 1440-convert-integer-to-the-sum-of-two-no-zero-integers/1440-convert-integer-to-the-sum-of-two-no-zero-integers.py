class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(n):
            if ('0' not in str(i)) and ('0' not in str(n-i)):
                return [i,n-i]