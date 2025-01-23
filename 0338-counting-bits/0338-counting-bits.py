class Solution(object):
    def countBits(self, n):
        l=[]
        l1=[]
        for i in range(n+1):
            l.append(bin(i)[2:])
        for i in l:
            l1.append(i.count('1'))
        return l1