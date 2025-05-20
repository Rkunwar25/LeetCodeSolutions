class Solution(object):
    def isFascinating(self, n):
       s=str(n)+str(n*2)+str(n*3)
       s1=sorted(list(set(s)))
       s2=list("123456789")
       return s1==s2 and len(s1)==len(s)