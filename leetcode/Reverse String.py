'''
easy
python : -> 의미, 함수 정의 시에 s: List[str], -> None

sol 1. 라이브러리 사용
reverse

sol 2. 라이브러리 없이
전체 합 구하는 공식처럼 reverse될 글자쌍을 서로 짝지어준다.
글자는 입력값이므로 접근할 때는 index 값으로 치환해서 생각하면 더 단순하다.
(0 1 2 3 4 5 를 5 4 3 2 1 0 으로 뒤집는다.)
index : 전체 string 길이를 측정 -> 0, n-1 관계로 swap

-> 응용 :
'''
# sol 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# sol 2 : wrong -> syntax error : left = 0, right = len(s) - 1
# wrong -> TypeError: '<' not supported between instances of 'tuple' and 'int'
#     while left < right:

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0, right = len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                # 위처럼 동시에 바꾸는 게 아니라, 아래처럼 줄 바꿈을 해도 결과가 동일할지 비교해보았다.
                # s[left] = s[right]
                # s[right] = s[left]
                left += 1
                right -= 1

# sol 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            # s[left], s[right] = s[right], s[left]
            s[left] = s[right]
            s[right] = s[left]
            left += 1
            right -= 1
'''
Your input
["h","e","l","l","o"]
Output
["o","l","l","l","o"]
Expected
["o","l","l","e","h"]
'''

# sol 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # swap 할 left 인덱스와 right 인덱스의 시작점 설정
        left, right = 0, len(s) - 1
        # left 인덱스와 right 인덱스가 같아지기 전까지
        while left < right:
            # swap
            s[left], s[right] = s[right], s[left]
            # left 인덱스는 +1 , right 인덱스는 -1 하면서 반복
            left += 1
            right -= 1