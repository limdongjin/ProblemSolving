#
# https://programmers.co.kr/learn/courses/30/lessons/42584
# 문제 제목: 주식가격
#


class Node:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx


def solution(prices):
    answer = []
    i = 0
    len_p = len(prices)
    for price in prices:
        if i + 1 == len_p:
            answer.append(0)
            break
        for j in range(i + 1, len_p):
            if prices[j] < price:
                answer.append(j - i)
                break
            elif j + 1 == len_p:
                answer.append(j - i)
        i += 1
    return answer


def test_solution():
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]


test_solution()
