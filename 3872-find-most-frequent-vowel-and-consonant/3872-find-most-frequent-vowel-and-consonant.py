class Solution(object):
    def maxFreqSum(self, s):
        count=Counter(s)
        v=[]
        c=[]
        for i,j in count.items():
            if i in 'aeiouAEIOU':
                v.append(j)
            elif i not in 'aeiouAEIOU':
                c.append(j)
        if len(c)==0 and len(v)==0:
            return 0
        elif len(v)==0:
            return max(c)
        elif len(c)==0:
            return max(v)
        else:
            return max(v)+max(c)