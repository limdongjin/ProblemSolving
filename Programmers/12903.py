#
# https://programmers.co.kr/learn/courses/30/lessons/12903
# 문제 제목: 가운데 글자 가져오기
#


def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1:len(s)//2 + 1]
    return s[len(s)//2]


def test_solution():
    assert solution("abcde") == "c"
    assert solution("qwer") == "we"


test_solution()