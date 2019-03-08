#
# https://programmers.co.kr/learn/courses/30/lessons/42840
# 문제 제목: 모의고사
#


def solution(answers):
    scores = [person_score(1, answers), person_score(2, answers), person_score(3, answers)]
    high_persons = [idx + 1 for idx, val in enumerate(scores) if val == max(scores)]
    return high_persons


def person_score(person_id, answers):
    return sum([is_answer(person_id, idx, val) for idx, val in enumerate(answers)])


def is_answer(person_id, problem_id, answer):
    if person_id is 1:
        person_ans = problem_id % 5 + 1
    elif person_id is 2 and problem_id % 2 is 0:
        person_ans = 2
    elif person_id is 2:
        person_ans = [1, 3, 4, 5][int((problem_id % 8) / 2)]
    else:
        person_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][problem_id % 10]
    return int(person_ans == answer)


def test_solution():
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]


test_solution()
