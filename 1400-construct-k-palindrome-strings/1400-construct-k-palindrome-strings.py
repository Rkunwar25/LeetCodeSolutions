from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        freq = Counter(s)
        odd_count = sum(1 for v in freq.values() if v % 2 == 1)
        
        return odd_count <= k
