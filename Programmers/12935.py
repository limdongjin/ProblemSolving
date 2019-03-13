#
# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3
# 문제 제목: 제일 작은수 제거하기
#


def solution(arr):
    min_arr = min(arr)
    answer = list(filter(lambda x: x != min_arr, arr))
    return answer if len(answer) != 0 else [-1]


def test_solution():
    assert solution([4, 3, 2, 1]) == [4, 3, 2]
    assert solution([10]) == [-1]


test_solution()