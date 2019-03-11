#
# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
# 문제 제목: 같은 숫자는 싫어
#


def solution(arr):
    answer = []
    bef = -1
    for a in arr:
        if bef == a:
            continue
        answer.append(a)
        bef = a
    return answer


def test_solution():
    assert solution([1,1,3,3,0,1,1]) == [1,3,0,1]
    assert solution([4,4,4,3,3]) == [4, 3]


test_solution()