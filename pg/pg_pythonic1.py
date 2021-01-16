# my answer -> more like c, java
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        j = len(mylist[i])
        answer.append(j)
    return answer

# pythonic
def solution(mylist):
    return list(map(len, mylist))