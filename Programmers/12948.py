#
# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
# 핸드폰 번호 가리기
#


def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]


def test_solution():
    assert solution("01033334444") == "*******4444"
    assert solution("027778888") == "*****8888"


test_solution()