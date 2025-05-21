class Solution(object):
    def areOccurrencesEqual(self, s):
        # c=Counter(s)
        # l=[]
        # for i,j in c.items():
        #     l.append(j)
        # return len(list(set(l)))==1
        return len(set(Counter(s).values())) == 1