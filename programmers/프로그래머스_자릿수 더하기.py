def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)):
        answer += int(n[i])

    return answer


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));