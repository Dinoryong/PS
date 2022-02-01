# 내가 풀은 틀린 답,, 마지막에 있는 공백 하나를 어떻게 없애지
def solution(s):
    answer = ''
    s = (s.split(" "))
    for i in range(len(s)):
        ls = len(s[i])
        print(s[i])
        answer += " "

        for j in range(ls):
            print(s[i][j])
            if j % 2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()

    return answer

# 성공
def solution(s):
    answer = ''
    s = (s.split(" "))
    for i in range(len(s)):
        ls = len(s[i])
        print(s[i])
        # answer += " "

        for j in range(ls):
            print(s[i][j])
            if j % 2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        answer += " "

    return answer[:-1]

