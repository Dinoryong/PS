def solution(a, b):
    answer = 1234567890
    temp = 0
    n = len(a)
    for i in range(0,n):
        temp += a[i]*b[i]

    return temp