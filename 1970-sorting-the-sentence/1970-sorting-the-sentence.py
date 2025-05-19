class Solution(object):
    def sortSentence(self, s):
        d=dict()
        s=s.split(' ')
        for i in s:
              d[int(i[-1])]=i[:-1]
        d=dict(sorted(d.items()))
        return " ".join(d.values())