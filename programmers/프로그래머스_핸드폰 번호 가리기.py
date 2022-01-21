def solution(phone_number):
    answer = ''

    i = len(phone_number[0:-4])
    # print(i)
    answer += "*" * i

    j = phone_number[-1:-5:-1]
    k = ""
    for t in range(3, -1, -1):
        k += j[t]
    answer += k

    return answer

#
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));

#
