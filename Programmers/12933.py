#
# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3
# 문제 제목: 정수 내림차순으로 배치하기
#


def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


def test_solution():
    print(solution(118372))
    assert solution(118372) == 873211


test_solution()