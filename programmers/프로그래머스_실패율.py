'''
처음 시도한 풀이
'''


def solution(N, stages):
    answer = []
    sum_tried = len(stages)
    result = {}
    for i in range(1, N + 1):
        temp = 0
        for j in range(len(stages)):
            if stages[j] == i:
                temp += 1
        result[i] = (temp / sum_tried)
        sum_tried -= temp

    # sorted_dict = result[1]
    sorted_value = []
    for i in range(1, N + 1):
        sorted_value.append(result[i])

    sorted_value.sort()
    # print(sorted_value)

    for value in sorted_value:
        if key, value in result.items():
            answer.append(key)
            del result[key]

    return answer

''' 틀린 답 : Runtime Error
for 문 2번 돌 때, 500*200,000=100,000,000 => 1억이라서
dictionary 를 value 기준으로 내림차순하는 방법
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
print(sorted_dict)
합계: 70.4 / 100.0
'''
def solution(N, stages):
    answer = []
    sum_tried = len(stages)
    result = {}
    for i in range(1, N + 1):
        temp = 0
        for j in range(len(stages)):
            if stages[j] == i:
                temp += 1
        result[i] = (temp / sum_tried)
        sum_tried -= temp

    sorted_dict = sorted(result.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict)
    for key in sorted_dict:
        answer.append(key[0])

    return answer

''' 
맞은 답

python count
'''
def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)