#
# https://programmers.co.kr/learn/courses/30/lessons/12944
# 문제 제목: 평균 구하기
#


def solution(arr):
    return sum(arr) / len(arr)


def test_solution():
    assert solution([1,2,3,4,5]) == 3
    assert solution([1, 2, 3, 4]) == 2.5
    assert solution(5, 5) == 5


test_solution()