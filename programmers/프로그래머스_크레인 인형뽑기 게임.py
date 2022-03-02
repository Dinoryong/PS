'''
IndexError
'''
def solution(board, moves):
    answer = 0

    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1] == bucket[-2]:  # list index out of range
                    answer += 1
                    bucket[:] = bucket[:-2]
                # break하면 i + 1 번째로 넘어가서 다시 check
                break
    return answer*2

''' 
정확성 100.0
'''
def solution(board, moves):
    answer = 0

    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += 1
                    bucket[:] = bucket[:-2]
                break
    return answer*2