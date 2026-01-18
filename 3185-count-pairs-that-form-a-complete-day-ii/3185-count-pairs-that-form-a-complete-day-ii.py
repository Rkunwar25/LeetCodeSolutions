class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = [0] * 24
        count = 0

        for h in hours:
            rem = h % 24
            needed = (24 - rem) % 24
            count += freq[needed]
            freq[rem] += 1

        return count
