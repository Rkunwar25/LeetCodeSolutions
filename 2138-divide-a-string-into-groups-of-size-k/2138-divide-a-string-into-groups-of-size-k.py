class Solution:
    def divideString(self, s: str, k: int, fill: str):
        res = []
        
        for i in range(0, len(s), k):
            part = s[i:i+k]
            if len(part) < k:
                part += fill * (k - len(part))
            res.append(part)
        
        return res
