class Solution(object):
    def rowAndMaximumOnes(self, mat):
        d=dict()
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
        mn=float('-inf')
        for i,j in d.items():
            mn=max(mn,j)
        l=[]
        for i in d.keys():
            if d[i]==mn:
                l.append(i)
        return [min(l),mn]