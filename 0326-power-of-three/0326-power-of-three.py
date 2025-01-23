class Solution(object):
    def isPowerOfThree(self, n):
        if(n==0):
            return False
        elif(n==1):
            return True
        else:
            while n%3==0 and n!=1:
                n=n/3
            if n%3!=0 and n!=1:
                return False
            else:
                return True