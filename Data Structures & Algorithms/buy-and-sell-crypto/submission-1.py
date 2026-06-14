class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0

        for R in range(L+1, len(prices)):
            print(L, R)
            current_profit = prices[R]-prices[L]
            if current_profit<0:
                L=R
            else:
                profit = max(profit, current_profit)

        return profit
