#
# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3
# x만큼 간격이 있는 n개의 숫자
#


def solution(x, n):
    k = 1 if x >= 0 else -1
    if x == 0:
        return [0 for e in range(0, n)]
    return list(range(x, n*x + k, x))


def test_solution():
    assert solution(2, 5) == [2,4,6,8,10]
    assert solution(4, 3) == [4,8,12]
    assert solution(-4, 2) == [-4, -8]
    assert solution(0, 2) == [0, 0]


test_solution()