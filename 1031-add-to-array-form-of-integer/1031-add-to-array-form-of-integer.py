class Solution(object):
    def addToArrayForm(self, num, k):
        s=""
        for i in num:
            s+=str(i)
        ans=int(s)+k
        l=[]
        for i in str(ans):
            l.append(int(i))
        return l