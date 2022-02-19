def solution(nums):
    answer = 0
    N = len(nums)

    set_nums = set(nums)
    # print(set_nums)
    k = len(set_nums)
    if k >= N/2:
        answer = N/2
    else:
        answer = k

    return answer
