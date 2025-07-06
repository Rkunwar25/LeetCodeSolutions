from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if abs(c1[ch] - c2[ch]) > 3:
                return False
        return True
