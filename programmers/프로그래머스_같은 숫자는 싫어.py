def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            pass
        else:
            answer.append(arr[i])

    return answer

# 리스트 슬라이싱은 빈 배열이어도 가능, 인덱싱은 불가능

