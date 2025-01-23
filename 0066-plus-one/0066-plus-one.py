class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s+=str(i)
        n=int(s)+1
        m=n
        l=[]
        while m!=0:
            l.append(m%10)
            m//=10
        return l[::-1]