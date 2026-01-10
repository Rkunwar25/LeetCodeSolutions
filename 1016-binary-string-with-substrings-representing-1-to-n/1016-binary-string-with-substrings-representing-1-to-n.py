class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            b = bin(i)[2:]
            if len(b) > len(s):
                return False
            if b not in s:
                return False
        return True
