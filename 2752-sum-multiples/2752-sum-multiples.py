class Solution(object):
    def sumOfMultiples(self, n):
        s=0
        for i in range(1,n+1):
            if i%5==0 or i%3==0 or i%7==0:
                s+=i
        return s