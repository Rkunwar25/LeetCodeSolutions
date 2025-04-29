class Solution(object):
    def bitwiseComplement(self, n):
        b=bin(n)
        s=str(b[2:])
        s1=''
        for i in s:
            if i=='0':
                s1+='1'
            else:
                s1+='0'
        
        return int(s1,2)
        