#
# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
#
def solution(name):
    answer = 0
    idxs = list(map(lambda x: x[0],
            list(filter(lambda x: x[1] !='A', enumerate(name)))))
    chars = []
    for ll in name:
        if ll != 'A':
            chars.append(min(ord(ll) - ord('A'), ord('Z')-ord(ll)+1))
    print(name)
    print(idxs)
    # print(chars)
    # print(name[idxs[0]])
    #print(answer)
    cursor = 0
    while len(idxs) != 0:
        zero = min(abs(idxs[0] - cursor), len(name) - abs(idxs[0] - cursor))
        last = min(abs(idxs[-1] - cursor), len(name) - abs(idxs[-1] - cursor))
        if zero <= last:
            cursor = idxs[0]
            answer += zero
            answer += chars[0]
            idxs.pop(0)
            chars.pop(0)
        else:
            cursor = idxs[-1]
            answer += last
            answer += chars[-1]
            idxs.pop(-1)
            chars.pop(-1)
    return answer
assert(solution("JAN") == 23)
assert(solution("JAZ") == 11)
assert(solution("JEROEN") == 56)

#print('a')
# AAAAAAAAAAAAAAA
# AAJAAZAABAAZCAA
# [2,5,11,12]

# AAAAAAAAAAAAAAA
# AZAABAAAAAAAAZA
# [1, 4, 13]
