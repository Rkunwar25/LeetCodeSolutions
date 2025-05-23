class Solution(object):
    def thousandSeparator(self, n):
        if len(str(n))<=3:
            return str(n)
        else:
            n=str(n)[::-1]
            s=""
            for i in range(len(n)):
                if i%3==0:
                    s+="."
                    s+=n[i]
                else:
                    s+=n[i]
            if s[len(s)-1]==".":
                s=s[:-1]
            s=s[::-1]
            if s[len(s)-1]==".":
                s=s[:-1]
            return s