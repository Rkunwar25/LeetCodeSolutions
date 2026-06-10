class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        m = min(len(s1), len(s2), len(s3))
        lcp = 0

        for i in range(m):
            if s1[i] == s2[i] == s3[i]:
                lcp += 1
            else:
                break

        if lcp == 0:
            return -1

        return (len(s1) - lcp) + (len(s2) - lcp) + (len(s3) - lcp)