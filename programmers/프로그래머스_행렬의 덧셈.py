def solution(arr1, arr2):
    # answer = [[]]
    n = len(arr1)

    arr = arr1[0]
    m = len(arr)
    answer = [[0 for j in range(m)] for i in range(n)]
    for a in range(0, n):
        for b in range(0, m):
            answer[a][b] = (arr1[a][b] + arr2[a][b])

    return answer

#
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A

#
def sumMatrix(A,B):
    n = len(A)
    m = len(A[0])

    answer = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

    return answer

#
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer