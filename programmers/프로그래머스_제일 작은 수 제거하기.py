def solution(arr):
    answer = []
    # 빈 배열인지 아닌지 확인하는 방법 : arr의 원소가 1또는 0이면 [-1] return
    if len(arr) <= 1:
        answer.append(-1)
    else:
        # answer.append((arr.remove(min(arr)))
        arr.remove(min(arr))
        answer = arr
    return answer



# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))



