'''
[sketch]
조합
아니다. 더 단순하게
오름차순으로 배열하고, 작은 예산부터 넣고
budget 이 0 미만 일 때면 그 전 index 값 return
'''


def solution(d, budget):
    answer = 0

    ds = sorted(d)

    for i in range(len(ds)):
        if (budget - ds[i]) >= 0:
            answer += 1
            budget = budget - ds[i]
        else:
            break

    return answer


# 다른 사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
