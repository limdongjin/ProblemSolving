from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(_) for _ in input().split()])
ans = []

for perm in permutations(A, M):
    ans.append(perm)

ans.sort()
for case in ans:
    print(' '.join(map(str, case)))