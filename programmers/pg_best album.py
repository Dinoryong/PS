"""
hash
생각대로 만들기가 어려웠다
python: lamda, zip, get(딕셔너리에서 key로 vaule 얻기)
"""
def solution(genres, plays):
    answer = []
    play_dic = {}  # {장르 : 총 재생 횟수}
    dic = {}  # {장르 : [(플레이 횟수, 고유번호)]}

    # hash
    for i in range(len(genres)):
        play_dic[genres[i]] = play_dic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]

    # 재생 횟수 내림차순으로 장르별 정렬
    genre_sort = sorted(play_dic.items(), key=lambda x: x[1], reverse=True)

    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genre_sort:
        dic[genre] = sorted(dic[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in dic[genre][:2]]

    return answer
""""""
# test를 위한 메인 함수
if __name__ == '__main__':
   genres = ["classic", "pop", "classic", "classic", "pop"]
   plays = [500, 600, 150, 800, 2500]
   result = solution(genres, plays)
   print(result)