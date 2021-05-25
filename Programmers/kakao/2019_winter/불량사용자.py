from itertools import product


def test_solution():
    assert solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]) == 2
    assert solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]) == 2
    assert solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]) == 3


def match_user(word, pattern):
    if len(word) != len(pattern):
        return False
    for i in range(len(word)):
        if pattern[i] != '*' and word[i] != pattern[i]:
            return False
    return True


def solution(user_id, banned_id):
    checked = [False] * len(user_id)
    cases = []

    def go(pid, cur_case):
        # banned[bid] 에 대응되는 패턴을 선택한다.
        if pid >= len(banned_id):
            if cur_case not in cases:
                cases.append(cur_case)
            return

        for user in range(len(user_id)):
            if checked[user] or not match_user(user_id[user], banned_id[pid]):
                continue

            checked[user] = True
            go(pid + 1, cur_case.union({user_id[user]}))
            checked[user] = False

        return

    go(0, set())
    return len(cases)


def solution2(user_id, banned_id):
    ans = set()
    cases = []
    for bid in range(len(banned_id)):
        cases.append([uid for uid in range(len(user_id))
                      if match_user(user_id[uid], banned_id[bid])])

    cases = list(product(*cases))
    for case in cases:
        if len(set(case)) == len(banned_id):
            ans.add(tuple(sorted(list(case))))

    return len(ans)


test_solution()
