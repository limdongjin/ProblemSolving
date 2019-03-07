#
# https://programmers.co.kr/learn/courses/30/lessons/42576
# 문제 제목: 완주하지 못한 선수
#


def solution(participant, completion):
    participant_h = {}
    completion_h = {}
    for person in participant:
        if participant_h.get(person) is None:
            participant_h[person] = 1
        else:
            participant_h[person] += 1
    for person in completion:
        if completion_h.get(person) is None:
            completion_h[person] = 1
        else:
            completion_h[person] += 1
    for person in participant:
        if participant_h.get(person) != completion_h.get(person):
            return person


def test_solution():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                    ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"],
                    ["stanko", "ana", "mislav"]) == "mislav"


test_solution()
