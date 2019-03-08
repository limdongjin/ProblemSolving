#
# https://programmers.co.kr/learn/courses/30/lessons/42840
# 문제 제목: 모의고사
#


def check_answer(person_id, problem_id, answer):
    checker = {
        1: {
            0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5
        },
        2: {
            1: 1,
            3: 3,
            5: 4,
            7: 5
        },
        3: {
            0: 3,
            1: 3,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
            6: 4,
            7: 4,
            8: 5,
            9: 5
        }
    }
    person_ans = 0
    if person_id == 1:
        person_ans = checker[person_id][problem_id % 5]
    elif person_id == 2 and problem_id % 2 == 0:
        person_ans = 2
    elif person_id == 2:
        person_ans = checker[person_id][problem_id % 8]
    else:
        person_ans = checker[person_id][problem_id % 10]
    return int(person_ans == answer)


def solution(answers):
    scores = [sum([check_answer(1, idx, val) for idx, val in enumerate(answers)]),
              sum([check_answer(2, idx, val) for idx, val in enumerate(answers)]),
              sum([check_answer(3, idx, val) for idx, val in enumerate(answers)])]
    high_persons = [idx + 1 for idx, val in enumerate(scores) if val == max(scores)]
    return high_persons


def test_solution():
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]


test_solution()