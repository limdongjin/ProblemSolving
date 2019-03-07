#
# https://programmers.co.kr/learn/courses/30/lessons/42588
# 문제 제목: 탑
#


def solution(heights):
    answer = []
    heights.reverse()
    i = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            if heights[j] > heights[i]:
                answer.append(len(heights) - j)
                break
            if j == len(heights) - 1:
                answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer


def test_solution():
    assert solution([6,9,5,7,4]) == [0,0,2,2,4]
    assert solution([3,9,9,3,5,7,2]) == [0,0,0,3,3,3,6]
    assert solution([1,5,3,6,7,6,5]) == [0,0,2,0,0,5,6]


test_solution()
