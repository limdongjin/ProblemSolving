def perms_iterative(s: str):
    ret = [""]

    for c in s:
        perms_from0_to_c = []    # 새로운 결과를 저장할 리스트
        for s1 in ret:  # 기존 결과 리스트에 있는 문자열들을 순회한다.
            perms_from0_to_c.extend(combination_str_and_c(s1, c)) # 해당 문자열(s1)과 문자(c)로 만들수있는 모든 경우를 저장
        ret = perms_from0_to_c
    return ret

def perms_stack(s: str):
    stack = []

    stack.append(s)
    for i in range(1, len(s)):
        stack.append(s[:-i])

    prev = []
    while stack:
        s1 = stack.pop()
        if len(s1) == 1:
            prev = [s1]
            continue
        ret = []
        for s2 in prev:
            ret.extend(combination_str_and_c(s2, s1[-1]))
        prev = ret

    return prev
def perms(s: str):
    if len(s) == 1:
        return [s]

    ret = perms(s[:-1])
    last_c = s[-1]
    new_ret = []
    for s1 in ret:
        new_ret.extend(combination_str_and_c(s1, last_c))

    return new_ret


def combination_str_and_c(original_str: str, c: str):
    ret = []

    for i in range(len(original_str)+1):
        ret.append(original_str[:i] + c + original_str[i:])

    return ret


s = "abcdef"

for perm in perms(s):
    print(perm, end=' ')
print()

for perm in perms_stack(s):
    print(perm, end=' ')
print()

for perm in perms_iterative(s):
    print(perm, end=' ')
print()
