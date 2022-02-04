def solution(a, b):
    answer = 0
    if a < b:
        answer = sum(i for i in range(a, b + 1))
    else:
        answer = sum(i for i in range(b, a + 1))

    return answer


#
def solution(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))