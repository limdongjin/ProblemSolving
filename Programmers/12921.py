#
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 문제 제목: 소수 찾기
#


def solution(n):
    if n == 2:
        return 1
    primes = [0, 0, 1, 1]
    for i in range(4, n + 1):
        primes.append(-1)
    for i in range(4, n + 1, 2):
        primes[i] = 0
    for i in range(6, n + 1, 3):
        primes[i] = 0
    for i in range(2, n + 1):
        if primes[i] != -1:
            continue
        primes[i] = 1
        for j in range(i*2, n + 1, i):
            primes[j] = 0
    return sum(primes)


def test_solution():
    assert solution(10) == 4
    assert solution(5) == 3


test_solution()