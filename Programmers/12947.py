#
# https://programmers.co.kr/learn/courses/30/lessons/12947
# 문제 제목: 하샤드 수
#


def solution(x):
    return x % sum([int(xx) for xx in str(x)]) == 0


def test_solution():
    assert solution(10) == True
    assert solution(12) == True
    assert solution(11) == False
    assert solution(13) == False


test_solution()