class Solution(object):
    def countGoodSubstrings(self, s):
        c=0
        s=list(s)
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==len(s[i:i+3]):
                c+=1
        return c