"""https://leetcode.com/problems/search-insert-position/"""
from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for elem in prices:
            if elem < buy:
                buy = elem
            elif elem - buy > profit:
                profit = elem - buy
        return profit
""" 
       buy = []
        sell = 0
        max_sell = 0
        if len(prices) <= 1:
            return 0
        buy.append(prices[0])
        for i in range(1, len(prices)):
            if prices[i] < buy[-1]:
                if sell > 0 :
                    if max_sell < sell:
                        max_sell = sell - buy[-1]
                    sell = 0
                buy.append(prices[i])
            elif sell < prices[i]:
                sell = prices[i]

        if sell > 0 and sell-buy[-1] > max_sell:
            return sell - buy[-1]
        else:
            return max_sell
"""


if __name__ == "__main__":
    solve = Solution()
    print(solve.maxProfit([3,2,6,5,0,3]))
