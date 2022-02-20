def solution(absolutes, signs):
    answer = 123456789
    result = 0
    for i in range(len(signs)):
        # print(signs[i])
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]
        # print(result)

    return result


# 한 줄로 굳이굳이 하자면
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))