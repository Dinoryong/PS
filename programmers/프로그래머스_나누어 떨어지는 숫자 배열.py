def solution(arr, divisor):
    answer = []

    # return [i if i % divisor == 0 else -1 break for i in arr]

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        else:
            pass

    answer.sort()

    if len(answer) == 0:
        answer.append(-1)

    return answer


# 내가 위에서 실패한 pythonic 풀이
def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]