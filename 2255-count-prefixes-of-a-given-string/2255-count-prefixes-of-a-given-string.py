class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for i in words:
            if s.startswith(i):
                c+=1
        return c