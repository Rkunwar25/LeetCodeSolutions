class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p=="*":
            return True
        p=p.split("*")
        p=list(filter(lambda x:x!="",p))
        if len(p)==1:
            return True if p[0] in s else False  
        if (p[0] not in s) or (p[1] not in s)      :
            return False
        i1=s.index(p[0])
        i2 = s.find(p[1], i1 + len(p[0]))         
        return True if i2 != -1 else False