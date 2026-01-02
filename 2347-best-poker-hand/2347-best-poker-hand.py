# from collections import Counter
# from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check Flush
        if len(set(suits)) == 1:
            return "Flush"
        
        rank_freq = Counter(ranks)
        max_count = max(rank_freq.values())
        
        # Check Three of a Kind
        if max_count >= 3:
            return "Three of a Kind"
        
        # Check Pair
        if max_count >= 2:
            return "Pair"
        
        return "High Card"
