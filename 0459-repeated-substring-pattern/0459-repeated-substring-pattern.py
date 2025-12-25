class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ns = ""
        n = len(s)        
        for i in range(n // 2):
            ns += s[i]
            if n % len(ns) == 0 and ns * (n // len(ns)) == s:
                return True        
        return False