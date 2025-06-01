class Solution(object):
    def checkIfPangram(self, sentence):
        s=set('abcdefghijklmnopqrstuvwxyz')
        return sorted(list(set(sentence)))==sorted(list(s))