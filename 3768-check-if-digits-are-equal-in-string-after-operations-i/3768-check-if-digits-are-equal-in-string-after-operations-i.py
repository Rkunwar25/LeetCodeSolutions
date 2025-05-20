class Solution(object):
    def hasSameDigits(self, s):
        def retMod(n):
            s=""
            for i in range(len(n)-1):
                s+=str((int(n[i])+int(n[i+1]))%10)
            return s
        while len(s)!=2:
            s=retMod(s)
        return s[0]==s[1]