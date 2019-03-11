#
# https://programmers.co.kr/learn/courses/30/lessons/12919
# 문제 제목: 서울에서 김서방 찾기
#


def solution(seoul):
    answer = ''
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"


def test_solution():
    assert solution(["Jane", "Kim"]) == "김서방은 1에 있다"


test_solution()
