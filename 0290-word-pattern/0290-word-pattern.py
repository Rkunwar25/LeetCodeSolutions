class Solution(object):
    def wordPattern(self, pattern, s):
        p=list(pattern)
        l=s.split(' ')
        if len(p)!=len(l):
            return False
        return [pattern.index(c) for c in pattern] == [l.index(w) for w in l]