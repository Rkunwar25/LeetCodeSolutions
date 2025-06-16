class Solution(object):
    def arrayRankTransform(self, arr):
        s=list(set(arr))
        s.sort()
        rank=dict()
        c=1
        for i in s:
            rank[i]=c
            c+=1
        l=[]
        for i in arr:
            l.append(rank[i])
        return l