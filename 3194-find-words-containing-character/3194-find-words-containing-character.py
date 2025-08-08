class Solution(object):
    def findWordsContaining(self, words, x):
        l=[i for i in range(len(words)) if x in words[i]]    
        return l