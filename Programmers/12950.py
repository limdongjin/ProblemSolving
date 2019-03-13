#
# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
# 행렬의 덧셈
#


def solution(arr1, arr2):
    ans = []
    yi = 0
    for y in arr1:
        sub_ans = []
        xi = 0
        for n in y:
            sub_ans.append(n + arr2[yi][xi])
            xi += 1
        ans.append(sub_ans)
        yi += 1
    return ans


def test_solution():
    assert solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]]
    assert solution([[1],[2]], [[3],[4]]) == [[4],[6]]


test_solution()