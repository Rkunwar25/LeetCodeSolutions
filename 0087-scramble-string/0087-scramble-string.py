class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            # Base case
            if a == b:
                memo[(a, b)] = True
                return True

            # Quick pruning: if they don’t even have same chars, can't be scramble
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)
            for i in range(1, n):  # try all split points
                # Case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Case 2: swap
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
