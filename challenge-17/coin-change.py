class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for value in range(1, amount + 1):
            for c in coins:
                if value - c >= 0:
                    dp[value] = min(dp[value], 1 + dp[value - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
                

# TC : O(N∗Amount)
# SC : O(Amount)