class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1]*n for i in range(2)]

        def stock(prices: List[int],buy: int, index: int, dp : List[List[int]], fee:int)-> int:
            n = len(prices)
            if index == n:
                return 0
            if dp[buy][index] != -1:
                return dp[buy][index]
            
            profit = 0

            if buy:
                buynow = -prices[index]+stock(prices,0,index+1,dp,fee)
                buylater = stock(prices,1,index+1,dp,fee)
                profit = max(buynow, buylater)
            else: #sell
                sellnow = prices[index]-fee+stock(prices,1,index+1,dp,fee)
                selllater = stock(prices,0,index+1,dp,fee)
                profit = max(sellnow, selllater)
            dp[buy][index] = profit
            return dp[buy][index]
            
        return stock(prices,1,0,dp,fee)