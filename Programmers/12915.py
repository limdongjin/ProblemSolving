#
# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
# 문제 제목: 문자열 내 마음대로 정렬하기
#


def solution(strings, n):
    answer = []
    char_h = {}
    for s in strings:
        if char_h.get(s[n]) is None:
            char_h[s[n]] = {}
            char_h[s[n]]['count'] = 1
            char_h[s[n]]['list'] = [s]
        else:
            char_h[s[n]]['count'] += 1
            char_h[s[n]]['list'].append(s)
    keys = list(char_h.keys())
    keys.sort()
    for key in keys:
        char_h[key]['list'].sort()
    for key in keys:
        for e in char_h[key]['list']:
            answer.append(e)
    return answer


def test_solution():
    assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
    assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]


test_solution()
