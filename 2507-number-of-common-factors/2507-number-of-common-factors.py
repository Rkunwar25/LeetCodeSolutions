class Solution(object):
    def commonFactors(self, a, b):
        small=a if a<b else b
        c=[i for i in range(1,small+1) if a%i==0 and b%i==0]
        return len(c)