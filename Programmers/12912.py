#
# https://programmers.co.kr/learn/courses/30/lessons/12912
# 문제 제목: 두 정수 사이의 합
#


def solution(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    return sum(range(a, b+1))


def test_solution():
    assert solution(3, 5) == 12
    assert solution(3, 3) == 3
    assert solution(5, 3) == 12

test_solution()