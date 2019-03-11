#
# https://programmers.co.kr/learn/courses/30/lessons/42748
# K 번째 수
#


def solution(array, commands):
    answer = []
    for command in commands:
        a = array[command[0] - 1:command[1]]
        a.sort()
        answer.append(a[command[2] - 1])
    return answer


def test_solution():
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]


test_solution()