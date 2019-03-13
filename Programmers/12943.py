#
# https://programmers.co.kr/learn/courses/30/lessons/12943
# 문제 제목: 콜라츠 추측
#


def solution(num):
    if num == 1:
        return 0
    for i in range(0, 500):
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1


def test_solution():
    assert solution(1) == 1
    assert solution(6) == 8
    assert solution(16) == 4
    assert solution(626331) == -1


test_solution()