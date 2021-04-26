"""
python: memoization (쥬니온유튭)
재미있는 DP
self._

간단하지만 뭔가 재밌는 문제였다

템플릿해두고
응용가능할듯
"""
class Solution:
    cache = {}
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            return self._climbStairs(n-1) + self._climbStairs(n-2)
    def _climbStairs(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]

