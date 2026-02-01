class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2
