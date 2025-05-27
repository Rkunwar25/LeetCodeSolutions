class Solution(object):
    def frequencySort(self, s):
        c=Counter(s)
        sc=sorted(c.items(),key= lambda x:(-x[1],x[0]))
        
        s=""
        for i,j in sc:
            s+=(i*j)
        return s
        