class Solution(object):
    def smallestEvenMultiple(self, n):
        c=n
        while True:
            if c%n==0 and c%2==0:
                return c
            c+=1 
