#
# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
# 문제 제목: 자릿수 더하기
#


def solution(n):
    return sum([int(num) for num in str(n)])


def test_solution():
    assert solution(123) == 6
    assert solution(987) == 24


test_solution()