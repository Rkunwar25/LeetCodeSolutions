class Solution(object):
    def findTheDifference(self, s, t):
        s1=list(s)
        t1=list(t)
        for i in s1:
            if i in t1:
                t1.remove(i)
        return ''.join(t1)