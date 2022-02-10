''' 틀린 답
테케3개맞춤/23개
정확성 17.4 / 100
'''
def solution(price, money, count):
    result = 0

    for i in range(count):
        if money - (price * (i + 1)) >= 0:
            money = money - (price * (i + 1))
        else:
            result = (price * (i + 1)) - money
            break
        # print(money)

    return result


''' 
테케 22개맞춤/23개
정확성 95.7 / 100
'''


def solution(price, money, count):
    result = 0

    for i in range(count):
        money = money - (price * (i + 1))

    if money >= 0:
        result = money
    else:
        result = -(money)

    return result


'''
맞는 답
문제 이해를 꼼꼼하게 하자!
'''
def solution(price, money, count):
    result = 0

    for i in range(count):
        money = money - (price * (i + 1))

    if money >= 0:
        result = 0
    else:
        result = -(money)

    return result