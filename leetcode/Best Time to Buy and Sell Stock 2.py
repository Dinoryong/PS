"""
swea 에서 백만장자였나 비슷한 문제를 본 것 같다.

Array, Greedy

prices = []
주의점 : 거래는 여러번 가능
"""
#
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit