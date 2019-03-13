#
# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
# 문제 제목: 약수의 합
#


def solution(n):
    answer = 0
    for num in range(1, n + 1):
        if n % num == 0:
            answer += num
    return answer


def test_solution():
    assert solution(12) == 28
    assert solution(5) == 6


test_solution()