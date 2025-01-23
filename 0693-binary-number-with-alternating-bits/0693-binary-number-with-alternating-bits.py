class Solution(object):
    def hasAlternatingBits(self, n):
        bn=bin(n)[2:]
        flag=0
        for i in range(len(bn)-1):
            if bn[i]!=bn[i+1]:
                continue
            else:
                flag=1
                break
        return flag==0