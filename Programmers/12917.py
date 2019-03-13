#
# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
# 문제 제목: 문자열 내림차순으로 배치하기
#


def solution(s):
    return "".join(sorted(s, reverse=True))


def test_solution():
    assert solution("bcdZefg") == "gfedcbZ"


test_solution()