class Solution(object):
    def isPalindrome(self, x):
        if x>=0: 
            x=str(x)      
            return x[::-1]==x
        else:
            return False