class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
         i=word.index(ch)
         l=word[:i+1]
         m=word[i+1:]
         n=l[::-1]
         return n+m 
        return word