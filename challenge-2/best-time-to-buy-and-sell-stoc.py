class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right, left = 1, 0
        profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                if profit < (prices[right] - prices[left]):
                    profit = prices[right] - prices[left]
            else:
                left = right
            right +=1
        return profit