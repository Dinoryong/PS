'''
zfill 없이 어떻게 처리할지는 len 길이에 따라서 앞에다가 len기준 - len현재 만큼 0을 더해주면 된다

파이썬에서 숫자를 출력하고자 할 때 , 앞에 0을 붙여주고 싶다면
zfill(width)
rjust(width, [fillchar])
'''
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)

    return answer