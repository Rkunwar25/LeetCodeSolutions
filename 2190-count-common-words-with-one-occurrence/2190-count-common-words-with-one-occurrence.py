class Solution(object):
    def countWords(self, words1, words2):
        l=words1 
        m=words2
        c=0
        for i in l:
            if (i in m) and (l.count(i)==1) and (m.count(i)==1):
                c+=1
        return c