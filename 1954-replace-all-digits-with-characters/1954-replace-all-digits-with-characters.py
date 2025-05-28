class Solution(object):
    def replaceDigits(self, s):
        s1=""
        n=len(s)
        for i in range(1,n,2):
            s1+=s[i-1]
            s1+=chr(ord(s[i-1])+int(s[i]))
        if n%2!=0:
            s1+=s[-1]
        return s1