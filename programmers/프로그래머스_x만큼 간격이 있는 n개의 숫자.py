def solution(x, n):
    answer = []
    a = 0
    for i in range(n):
        a += x
        answer.append(a)
    return answer