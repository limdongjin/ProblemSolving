#
# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
# 문제 제목: 위장
#
def solution(clothes):
    answer = 0
    clothe_types_h = {}
    for clothe in clothes:
        if clothe_types_h.get(clothe[1]) is None:
            clothe_types_h[clothe[1]] = 1
        else:
            clothe_types_h[clothe[1]] += 1
    if len(clothe_types_h.keys()) == 1:
        return len(clothes)
    else:
        answer = 1
        for key in clothe_types_h:
            answer *= (clothe_types_h[key] + 1)

    return answer - 1



def test_solution():
    assert solution([["yellow_hat", "headgear"],
                     ["blue_sunglasses", "eyewear"],
                     ["green_turban", "headgear"]]) == 5
    assert solution([["crow_mask", "a"],
                     ["blue_sunglasses", "b"],
                     ["smoky_makeup", "c"]]) == 7


test_solution()