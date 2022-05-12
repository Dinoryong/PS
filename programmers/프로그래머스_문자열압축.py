"""

"""
def solution(s):
    length = []
    result = ""

    # s 의 총길이가 1이라면 비교대상 없이, 바로 1을 리턴한다.
    if len(s) == 1:
        return 1

    # 문자열을 자르는 단위는 cut
    # cut 의 범위는 총 문자열 s 길이의 절반을 넘어갈 필요가 없다.
    for cut in range(1, len(s) // 2 + 1):
        # count 는 문자열 반복 단위 횟수로, 처음에는 1로 초기화한다.
        # tempStr 은 문자열에서 처음부터 문자열 반복 단위 까지 자른 문자열이다.
        count = 1
        tempStr = s[:cut]
        # cut (문자열 단위)만큼, 건너뛰면서 반복한다.
        for i in range(cut, len(s), cut):
            # 이전 문자열과 그 다음 건너뛴 문자열이 같다면, count 값을 1 올려준다.
            if s[i:i + cut] == tempStr:
                count += 1
            # 다르다면
            # count 값이 1일 경우에는 생략하기 위해 string 빈 값으로 주고
            # 최종 결과에는 문자열반복단위를 문자열로 바꾼 후에 tempStr과 합쳐준다.
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                # tempStr 은 그 다음 반복문자열을 찾기 위해 갱신해준다
                # count 도 마찬가지로 갱신해준다.
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)



# sol.2
def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):

            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1

            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 초기화
                count = 1  # count도 초기화

        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev

        # 만들어지는 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer