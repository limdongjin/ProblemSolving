from itertools import permutations

N, M = map(int, input().split())
A = sorted([int(_) for _ in input().split()])

ans = []
for perm in permutations(A, M):
    ans.append(perm)

ans = list(set(ans))
ans.sort()

for case in ans:
    print(' '.join(map(str, case)))