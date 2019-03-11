#
# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
# 문제 제목: 체육복
#


def solution(n, lost, reserve):
    answer = n - len(lost)
    new_lost = []
    for l in lost:
        if reserve.count(l) != 0:
            reserve.remove(l)
            answer += 1
            continue
        new_lost.append(l)
    for l in new_lost:
        if reserve.count(l + 1) != 0:
            reserve.remove(l + 1)
            answer += 1
        elif reserve.count(l - 1) != 0:
            reserve.remove(l - 1)
            answer += 1
    return answer


def test_solution():
    assert solution(5, [2, 4], [1, 3, 5]) == 5
    assert solution(5, [2, 4], [3]) == 4
    assert solution(3, [3], [1]) == 2
    assert solution(5, [2, 4], [2, 3]) == 5


test_solution()