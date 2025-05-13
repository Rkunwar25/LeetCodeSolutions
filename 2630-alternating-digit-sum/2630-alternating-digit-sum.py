class Solution(object):
    def alternateDigitSum(self, n):
        s=0
        n=str(n)
        s=int(n[0])
        flag=1
        for i in n[1:] :
            flag*=-1
            s+=(flag*int(i))
        return s