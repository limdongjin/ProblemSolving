#
# https://programmers.co.kr/learn/courses/30/lessons/12930
# 문제 제목: 이상한 문자 만들기
#


def solution(s):
    answer = ""
    strings = s.split(sep=' ')
    print(strings)
    for ss in strings:
        i = 0
        if ss == '':
            answer += " "
            continue
        for st in ss:
            if i % 2 == 0:
                answer += st.capitalize()
            else:
                answer += st.lower()
            i += 1
        answer += " "
    return answer[:-1]


def test_solution():
    assert solution("try hello world") == "TrY HeLlO WoRlD"


test_solution()