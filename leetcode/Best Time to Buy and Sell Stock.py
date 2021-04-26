"""
swea 백만장자와 비슷한 문제

완탐이라고는 하는데, 더 줄일 수 없을까?
간단해서 더 찝찝했다.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            buy = prices[0]
            mx_profit = 0

            for i in range(1,len(prices)):
                profit = prices[i]-buy

                if profit>mx_profit:
                    mx_profit = profit

                if buy>prices[i]:
                    buy = prices[i]

            return mx_profit

