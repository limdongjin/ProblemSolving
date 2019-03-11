#
# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
# 문제 제목: 카펫
#


def solution(brown, red):
    size = brown + red
    for x in range(1, size):
        y = size // x
        if x < y:
            continue
        if x + x + y + y - 4 == brown:
            return [x, y]


def test_solution():
    assert solution(10, 2) == [4, 3]
    assert solution(8, 1) == [3, 3]
    assert solution(24, 24) == [8, 6]


test_solution()