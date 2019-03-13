#
# https://programmers.co.kr/learn/courses/30/lessons/12937
# 문제 제목: 짝수와 홀수
#


def solution(num):
    return "Even" if num % 2 is 0 else "Odd"


def test_solution():
    assert solution(3) == "Odd"
    assert solution(4) == "Even"


test_solution()