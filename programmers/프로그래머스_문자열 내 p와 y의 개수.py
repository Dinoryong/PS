def solution(s):
    answer = True
    # ans1, ans2 = 0
    ans1 = 0
    ans2 = 0

    s = s.upper()

    for i in range(len(s)):
        print(s[i])
        if s[i] == 'P':
            ans1 += 1
        elif s[i] == 'Y':
            ans2 += 1
        else:
            pass

    if (ans1 == ans2) or (ans1 == ans2 == 0):
        pass
    else:
        answer = False

    return answer

# pythonic 하게 다시 풀기
def solution(s):
    return s.upper().count("P") == s.upper().count("Y")