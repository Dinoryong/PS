'''
<list>.sort() 메서드 vs sorted(<list>) built-in 함수

https://inma.tistory.com/137

'''
def solution(s):
    return "".join(sorted(s, reverse=True))