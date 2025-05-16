class Solution(object):
    def mostWordsFound(self, sentences):
        l=[]
        for i in sentences:
            l.append(len(i.split(' ')))
        return max(l)