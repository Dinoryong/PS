def solution(str1, str2):

    # 교집합 원소의 개수
    def intersection_set(A, B):
        n = 0
        for x in set(A):
            if x in B:
                n += min(A.count(x), B.count(x))
        return n

    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    A, B = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            A.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            B.append(str2[i] + str2[i + 1])

    # Edge case A,B 모두가 공집합인 경우에 자카드 유사도는 1
    if (not A) and (not B):
        return 65536

    # 교집합의 원소의 개수 구하기
    n = intersection_set(A, B) if len(A) < len(B) else intersection_set(B,A)

    answer = n / (len(A) + len(B) - n)

    return int(answer * 65536)