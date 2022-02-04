#
def solution(seoul):
    idx = 0
    answer = 0
    # answer = print(f'김서방은 {idx}에 있다')

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            idx = str(i)
    answer = '김서방은 ' + idx + '에 있다'
    return answer

#
def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"