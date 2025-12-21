class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.split("-")
        for i in range(len(s)):
            s[i]=s[i].upper()
        s="".join(s)   
        s=s[::-1]
        ns=""
        i=0
        n=len(s)
        while i<n:
            if (n-i)<=k:
                ns+=s[i:]
                break
            ns+=s[i:i+k]+"-"
            i+=k
        ns=ns[::-1]
        return ns