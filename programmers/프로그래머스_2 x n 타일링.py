def solution(n):
    answer = 0
    d = [0] * 60001
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1000000007

    return d[n]