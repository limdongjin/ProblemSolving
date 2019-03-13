#
# https://programmers.co.kr/learn/courses/30/lessons/12940
# 문제 제목: 최대 공약수와 최소 공배수
#


def solution(n, m):
    gcd = max(set([x for x in range(1, n + 1) if n % x == 0]) &
                set([x for x in range(1, m + 1) if m % x == 0]))
    return [gcd,
            gcd * (n // gcd) * (m // gcd)]


def test_solution():
    assert solution(3, 12) == [3, 12]
    assert solution(2, 5) == [1, 10]


test_solution()