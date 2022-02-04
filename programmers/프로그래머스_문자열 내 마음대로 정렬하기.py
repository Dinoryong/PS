'''
python dictionary에서 key 혹은 value 기준 정렬하기
https://codechacha.com/ko/python-sorting-dict/#:~:text=Key%EB%A5%BC%20%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C%20%EC%A0%95%EB%A0%AC%20(%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C),%EC%9D%98%20key%EB%A5%BC%20%EC%9D%98%EB%AF%B8%ED%95%A9%EB%8B%88%EB%8B%A4.
'''
def solution(strings, n):
    answer = []
    # 사전순으로 정렬
    strings.sort()
    # print(strings)
    f = {}  # key : 단어 , value : n번째 인덱스 알파벳
    for i in range(len(strings)):
        f[strings[i]] = strings[i][n]
    print(f)

    # value 기준으로 오름차순 sorted
    sorted_f = sorted(f.items(), key=lambda item: item[1])

    print(sorted_f)
    for key in sorted_f:
        answer.append(key[0])

    return answer

