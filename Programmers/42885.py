
def solution(people, limit):
    answer = 0
    cur = 0
    idx = 0
    st = 0
    people.sort()
    # [50, 50, 70, 80], 100
    len_p = len(people)
    last = len_p - 1
    while len_p > 0:
        if people[last] + people[st] <= limit and len_p != 1:
            answer += 1
            # people.pop(0)
            # people.pop(-1)
            st += 1
            last -= 1
            len_p -= 2
        elif len_p == 1:
            answer += 1
            # people.pop(-1)
            len_p = 0
            break
        else:
            answer += 1
            # people.pop(-1)
            last -= 1
            len_p -= 1
    return answer

assert(solution([70, 50, 80, 50],100) == 3)
assert(solution([70, 80, 50], 100) == 3)
assert(solution([50, 50, 50, 50], 200) == 2)
assert(solution([50, 60, 50, 50], 200) == 2)
assert(solution([40, 40, 240, 100, 240], 240) == 4)
assert(solution([80, 100, 130, 200, 40], 210) == 3)

