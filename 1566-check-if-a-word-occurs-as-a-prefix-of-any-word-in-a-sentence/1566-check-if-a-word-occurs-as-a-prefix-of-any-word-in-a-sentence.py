class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        res=-1
        l=sentence.split(' ')
        n=len(searchWord)
        for i in range(len(l)):
            if searchWord == l[i][:n]:
                res=i+1
                break
        return res