from typing import List


def test_solution():
    assert solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
    assert solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
    assert solution("{{20,111},{111}}") == [111, 20]
    assert solution("{{123}}") == [123]
    assert solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]


def get_setlist(s):
    ret = [set(map(int, ss.split(',')))
           for ss in s[2:-2].split('},{')]
    return ret


def solution(s):
    answer = []

    setlist: List[set] = get_setlist(s)
    setlist.sort(key=len)

    prev_sum = 0
    for sett in setlist:
        v = sum(sett) - prev_sum
        answer.append(v)
        prev_sum += v

    return answer


test_solution()
