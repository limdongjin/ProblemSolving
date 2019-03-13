#
# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
# 예산
#


def solution(d, budget):
    d.sort()
    res = 0
    i = 0
    for dd in d:
        if dd + res > budget:
            return i
        elif dd + res == budget:
            return i + 1
        res += dd
        i += 1
    return i


def test_solution():
    assert solution([1,3,2,5,4], 9) == 3
    assert solution([2, 2, 3, 3], 10) == 4


test_solution()