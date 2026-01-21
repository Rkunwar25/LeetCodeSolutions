class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        n = len(s)
        i = 0

        while i < n:
            start = i
            while i + 1 < n and s[i] == s[i + 1]:
                i += 1
            
            if i - start + 1 >= 3:
                res.append([start, i])
            
            i += 1
        
        return res
