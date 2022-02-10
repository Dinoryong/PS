'''
맞긴 했는데
range 범위를 줄여줘야할듯
'''
def solution(n):
    answer = 0

    for x in range(2, n + 1):
        if n % x == 1:
            answer = x
            break

    return answer