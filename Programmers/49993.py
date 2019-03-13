#
# https://programmers.co.kr/learn/courses/30/lessons/49993
# 스킬트리
#


def solution(skill, skill_trees):
    answer = 0
    skill_trees2 = []
    for ski in skill_trees:
        skill_trees2.append("".join(list(filter(lambda x: skill.count(x) != 0, ski))))
    for ski in skill_trees2:
        sk = skill
        flag = 1
        for s in ski:
            if s != sk[0]:
                flag = 0
                break
            else:
                sk = sk[1:]
                if len(sk) == 0:
                    flag = 1
                    break
        if flag == 1:
            answer += 1
    return answer


def test_solution():
    assert solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2


test_solution()