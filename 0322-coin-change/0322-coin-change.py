class Solution(object):
    def coinChange(self, coins, amount):
        # Initialize DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins to make amount 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
