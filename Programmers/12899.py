#
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
# 124나라의 숫자
#


def solution(n):
    ptmap = [1]
    for i in range(1, 19):
        ptmap.append(ptmap[i-1] + pow(3, i))
    d = 0
    res = 0
    for t in ptmap:
        if t > n:
            break
        d += 1
        res = n - t
    result = ["1"]*d
    result_len = len(result)
    if res == 0:
        return "".join(result)
    for dd in range(d, -1, -1):
        pow_dd = pow(3, dd)
        for i in range(0, 3):
            if res - pow_dd < 0:
                break
            idx = result_len - dd - 1
            res -= pow_dd
            result[idx] = str(int(result[idx]) + 1)
            if result[idx] == "3":
                result[idx] = "4"
    return "".join(result)


def test_solution():
    assert solution(1) == "1"
    assert solution(2) == "2"
    assert solution(3) == "4"
    assert solution(4) == "11"
    assert solution(18) == "124"
    assert solution(22) == "211"


test_solution()