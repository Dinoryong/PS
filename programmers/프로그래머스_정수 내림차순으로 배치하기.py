# 틀린 solution
def solution(n):
    n = str(n)
    temp = []
    answer = ""
    for i in range(1, len(n)):
        temp.append(n[i])
    for k in range(1, len(temp)):
        if temp[k - 1] > temp[k]:
            temp[k] = temp[k - 1]
            temp[k - 1] = temp[k]
    print(temp)

    for j in range(len(temp)):
        answer += temp[j]

    return answer


#
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int("".join(n))