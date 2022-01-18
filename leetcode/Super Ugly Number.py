# heap
'''
(ugly, primei)
'''
class a:
	def __init__(self, tup):
		self.tup = tup

	def __lt__(self, other):
		return self.tup[0] < other.tup[0]


class Solution:
	def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
		m = len(primes)
		pq = []
		isin = set()
		res = [1]
		li = [0] * 100
		for i in range(m):
			heappush(pq, a((primes[i], i)))
		count = 1
		while (count < n):
			now, j = heappop(pq).tup
			li[j] += 1
			if now not in isin:
				isin.add(now)
				res.append(now)
				count += 1
			heappush(pq, a((res[li[j]] * primes[j], j)))

		return res[-1]


#
def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
	out = [1]
	x = 2
	while len(out) != n:
		temp = x
		for p in primes:
			while temp % p == 0:
				temp = temp//p

		if temp == 1:
			out.append(x)

		x += 1

	return out[-1]

#
from heapq import heappush, heappop


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        lst = [1]*(n+1)
        k = len(primes)
        indices = [0] * k
        heap = []
        for i, p in enumerate(primes):
            heappush(heap, (p, i))
        index = 0
        while index < n:
            (min_elem, index_min_elem) = heappop(heap)
            if min_elem != lst[index]:
                index += 1
                lst[index] = min_elem
            indices[index_min_elem] += 1
            heappush(heap, (primes[index_min_elem]*lst[indices[index_min_elem]],index_min_elem))
        return lst[n-1]

#
class Solution:
	def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
		m_list = [0] * len(primes)
		ret_list = [1]
		possible_nums = [p for p in primes]

		while len(ret_list) < n:
			minimum = min(possible_nums)
			if minimum != ret_list[-1]:
				ret_list.append(minimum)
			min_idx = possible_nums.index(minimum)
			m_list[min_idx] += 1
			# The main DP step
			# Update the possible numbers to add to return list
			possible_nums[min_idx] = primes[min_idx] * ret_list[m_list[min_idx]]

		return ret_list[-1]

