class Solution(object):
    def findLucky(self, arr):
        c=Counter(arr)
        l=[]
        for i,j in c.items():
            if i==j:
                l.append(i)
        if l:
            return max(l)
        return -1