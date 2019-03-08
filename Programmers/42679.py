#
# https://programmers.co.kr/learn/courses/30/lessons/42579
# 문제 제목: 베스트 앨범
#
class Node:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
def solution(genres, plays):
    answer = []
    genres_count_h = {}
    genre_song_h = {}
    count_genre_h = {}
    i = 0
    for genre in genres:
        if genres_count_h.get(genre) is None:
            genres_count_h[genre] = plays[i]
            genre_song_h[genre] = [Node(plays[i], i)]
        else:
            genres_count_h[genre] += plays[i]
            genre_song_h[genre].append(Node(plays[i], i))
        i += 1
    for key in genres_count_h:
        count_genre_h[genres_count_h[key]] = key
    ckeys = list(count_genre_h.keys())
    # print(ckeys)
    ckeys.sort()
    ckeys.reverse()
    # print(genres_count_h)
    # print(ckeys)
    for key in ckeys:
        genre = count_genre_h[key]
        f_num = -1
        f_idx = -1
        s_num = -1
        s_idx = -1
        for song_node in genre_song_h[genre]:
            if f_num < song_node.value:
                f_num = song_node.value
                f_idx = song_node.idx
        for song_node in genre_song_h[genre]:
            if f_num == song_node.value and f_idx != song_node.idx:
                s_num = song_node.value
                s_idx = song_node.idx
                break
            if s_num < song_node.value and f_idx != song_node.idx:
                s_num = song_node.value
                s_idx = song_node.idx
        if s_num == -1:
            answer.append(f_idx)
        else:
            answer.extend([f_idx, s_idx])
    return answer


def test_solution():
    assert solution(["classic", "pop", "classic", "classic", "pop"],
                    [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
    assert solution(["classic", "pop", "classic", "classic", "pop"],
                    [500, 600, 500, 800, 300]) == [3, 0, 1, 4]

test_solution()