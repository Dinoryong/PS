def solution(numbers):
    # answer = -1
    answer = sum(i for i in range(10))
    # print(answer)
    for i in range(len(numbers)):
        answer -= numbers[i]

    return answer