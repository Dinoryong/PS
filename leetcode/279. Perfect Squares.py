# 여기까지 떠올림..
class Solution:
    def numSquares(self, n: int) -> int:
        temp = []
        for i in range(1, n+1):
            if (i**2) <= n:
                temp.append((i**2))
        print(temp)

'''

'''
class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)