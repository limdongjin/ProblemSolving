#
# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
# 문제 제목: 정수 제곱근 판별
#


def solution(n):
    for i in range(1, n + 1):
        if i*i == n:
            return (i+1)*(i+1)
        elif i*i > n:
            break
    return -1


def test_solution():
    assert solution(121) == 144
    assert solution(3) == -1
    assert solution(100) == 121
    assert solution(144) == 169
    assert solution(1) == 4


test_solution()