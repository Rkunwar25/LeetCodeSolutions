class Solution(object):
    def truncateSentence(self, s, k):
        s1=s.split()        
        s1=s1[:k]
        return " ".join(s1)