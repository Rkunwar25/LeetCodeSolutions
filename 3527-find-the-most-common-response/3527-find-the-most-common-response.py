from collections import Counter
from typing import List

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = Counter()
        
        for resp in responses:
            freq.update(set(resp))
        
        # Sort lexicographically first, then pick max by frequency
        return max(sorted(freq.keys()), key=lambda w: freq[w])
