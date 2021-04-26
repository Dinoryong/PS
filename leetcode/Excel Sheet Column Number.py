"""
1부터 26까지라고 생각
ord 함수 : 아스키코드 변환
chr 함수와 반대임
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26
            result += (ord(columnTitle[i]) - ord('A') + 1)
        return result