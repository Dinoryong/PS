#
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        num -= set(range(2*i,n+1,i))
    return len(num)

# 왜 if 부분을 추가한 방법으로 많이 풀었지
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)