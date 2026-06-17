

'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
'''

class solution:
    def maxprofit(self, prices):
        n = len(prices)

        # dp[i][0] at the end of the day i, max profit when holding the stock
        # dp[i][1] at the end of the day i, max profit when not holding the stock
        dp = [[0,0] for _ in range(n)]

        # hold stock at day 0 = buy stock
        dp[0][0] = -prices[0]

        # not hold stock at day 0 = do nothing
        dp[0][1] = 0

        for i in range(1, n):

            # hold stock at day i = 1. hold yesterday or 2. buy today
            dp[i][0] = max(dp[i - 1][0], -prices[i])

            # not hold stock at day i = 1. not hold yestoday or 2. sold today
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[n - 1][1] #最后一天卖出股票赚的钱


sol = solution()
prices = [10,1,5,6,7,1]

print(sol.maxprofit(prices))


