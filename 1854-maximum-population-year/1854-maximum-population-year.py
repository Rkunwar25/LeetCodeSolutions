class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l=[]
        for i in logs:
            l.extend(list(range(i[0],i[-1])))
        l.sort()
        nl=sorted(list(set(l)))
        mx=float('-inf')
        year=0
        for i in nl:
            if l.count(i)>mx:
                year=i
                mx=l.count(i)
        return year