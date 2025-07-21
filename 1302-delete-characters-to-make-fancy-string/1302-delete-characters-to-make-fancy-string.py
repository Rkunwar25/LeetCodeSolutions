class Solution(object):
    def makeFancyString(self, s):
        c=""
        n=len(s)
        for i in range(n):
            if not c:
                c+=s[i]
            elif len(c)>=2 and c[len(c)-1]==c[len(c)-2]==s[i]:
                    continue
            else:
                c+=s[i]
        return c