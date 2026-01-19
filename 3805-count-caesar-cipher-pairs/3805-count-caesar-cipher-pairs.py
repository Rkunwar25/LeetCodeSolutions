from collections import defaultdict

class Solution:
    def countPairs(self, words):
        def normalize(word):
            shift = ord(word[0]) - ord('a')
            return ''.join(
                chr((ord(c) - shift - ord('a')) % 26 + ord('a'))
                for c in word
            )

        freq = defaultdict(int)

        for w in words:
            key = normalize(w)
            freq[key] += 1

        ans = 0
        for count in freq.values():
            ans += count * (count - 1) // 2

        return ans
