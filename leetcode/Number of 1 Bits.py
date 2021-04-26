"""
1 bits 보고
비트연산이 떠올라서 갑자기 비트연산 복습ㅋㅋ

 Hamming weight
"""
class Solution(object):
def hammingWeight(self, n):
"""
:type n: int
:rtype: int
"""
return bin(n).count('1')
