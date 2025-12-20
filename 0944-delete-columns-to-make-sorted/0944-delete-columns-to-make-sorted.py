class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ls=[]
        for i in strs:
            ls.append(list(i))
        ls=list(map(list,zip(*ls)))
        c=0
        for i in range(len(ls)):
            if ls[i]!=sorted(ls[i]):
                c+=1
        return c