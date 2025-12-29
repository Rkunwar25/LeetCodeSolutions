from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: count letters in licensePlate
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        ans = None
        
        # Step 2: check each word
        for word in words:
            cnt = Counter(word.lower())
            
            # check if word completes licensePlate
            if all(cnt[c] >= need[c] for c in need):
                if ans is None or len(word) < len(ans):
                    ans = word
        
        return ans
