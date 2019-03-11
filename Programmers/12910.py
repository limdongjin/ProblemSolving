#
# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
# 문제 제목: 나누어떨어지는 숫자배열
#



def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer


def test_solution():
    assert solution([5, 9, 7, 10], 5) == [5, 10]
    assert solution([2, 36, 1, 3], 1) == [1, 2, 3, 36]
    assert solution([3, 2, 6], 10) == [-1]

test_solution()