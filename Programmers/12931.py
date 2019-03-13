#
# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
# 문제 제목: 자릿수 더하기
#


def solution(n):
    return sum([int(num) for num in str(n)])


def solution2(n):
    return sum(map(int, str(n)))


def test_solution():
    assert solution(123) == 6
    assert solution(987) == 24


def test_solution2():
    assert solution(123) == 6
    assert solution(987) == 24


test_solution()
test_solution2()