'''
아이디어를 생각 못 하고 뭔가 어렵게 풀려고 했다
'''
def solution(sizes):
    answer = 0
    heights, widths = {}, {}

    for i in range(len(sizes)):
        widths[i] = sizes[i][0]
        heights[i] = sizes[i][1]
    print(max(widths))
    #     print(max(widths))
    #     print(max(heights))

    return answer
''' 
[sketch]
각 명함의 가로 , 세로 중에서 더 긴 값을 첫번째로 정렬하고
첫번째 값들을 가로 길이 후보, 두번째 값들을 세로 길이 후보로 정한다
'''
def solution(sizes):
    widths, heights = [], []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
        widths.append(sizes[i][0])
        heights.append(sizes[i][1])
    answer = max(widths) * max(heights)

    return answer

'''
큰 값들 중에서 젤 큰 것과 작은 값들 중에서 제일 큰 것 곱하기
'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)