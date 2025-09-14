class Solution(object):
    def numSquares(self, n):
        # Precompute all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # DP array where dp[i] = fewest number of perfect squares summing to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for s in squares:
                if s > i:
                    break
                dp[i] = min(dp[i], dp[i - s] + 1)

        return dp[n]
