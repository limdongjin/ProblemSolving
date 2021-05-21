from sys import stdin
input = stdin.readline

def solve(s):
    stack = []

    for br in s:
        if br == open_br:
            stack.append(br)
            continue
        if not stack:
            return False
        stack.pop()
    if stack:
        return False
    return True

open_br = '('
close_br = ')'
ans = []
for _ in range(int(input())):
    S = input().rstrip()

    if solve(S):
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))
