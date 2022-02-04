# 틀린 답 : 정확성 87.5/100
'''
공백은 어떻게하는것이지'''
def solution(s):
    answer = True
    if len(s) == 4 or 6:
        for i in range(len(s)):
            if s[i].isdigit():
                pass
            else:
                answer = False
    else:
        answer = False

    return answer

# 고친 답
''' 
or를 쓸 때 잘못 써서 test case 5,6이 계속 틀렸었다.반성!!
'''
def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isalnum():
            if s.isdigit():
                pass
            else:
                answer = False
        else:
            answer = False
    else:
        answer = False

    return answer
