class Solution(object):
    def prefixCount(self, words, pref):
        c=0
        for i in words:
            if i.startswith(pref):
                c+=1
        return c