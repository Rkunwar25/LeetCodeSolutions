class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = Counter()
        
        for resp in responses:
            freq.update(set(resp))
        return max(sorted(freq.keys()), key=lambda w: freq[w])