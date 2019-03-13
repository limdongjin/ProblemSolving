#
# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3
# 문제 제목: 문자열 다루기 기본
#


def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for c in s:
        if '0' > c:
            return False
        elif '9' < c:
            return False
    return True


def test_solution():
    assert solution("a234") is False
    assert solution("1234") is True


test_solution()