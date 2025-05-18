class Solution(object):
    def maxDifference(self, s):
        c=Counter(s)
        odd=[]
        even=[]
        for i,j in c.items():
            if j%2==0:
                even.append(j)
            else:
                odd.append(j)
        return max(odd)-min(even)