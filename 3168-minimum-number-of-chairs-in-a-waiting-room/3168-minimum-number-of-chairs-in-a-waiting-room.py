class Solution:
    def minimumChairs(self, s: str) -> int:
        curr = 0
        ans = 0

        for ch in s:
            if ch == 'E':
                curr += 1
                ans = max(ans, curr)
            else:
                curr -= 1

        return ans