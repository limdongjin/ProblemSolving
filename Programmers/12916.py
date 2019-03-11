#
# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문제 제목: 문자열 내 p와 y의 개수
#
def solution(s):
    s = s.lower()
    if s.count("p") == s.count("y"):
        return True
    return False

def test_solution():
    assert solution("pPoooyY") == True
    assert solution("Pyy") == False


test_solution()