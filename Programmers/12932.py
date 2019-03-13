#
# https://programmers.co.kr/learn/courses/30/lessons/12932
# 문제 제목: 자연수 뒤집어 배열로 만들기
#


def solution(n):
    return list(reversed(list(map(int, str(n)))))


def test_solution():
    print(solution(12435))
    assert solution(12435) == [5, 3, 4, 2, 1]
    assert solution(2191) == [1, 9, 1, 2]


test_solution()