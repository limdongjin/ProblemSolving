import sys
from collections import deque

N = int(input())
# cr
A = [int(_) for _ in input().split()]
M = int(input())
# box
B = [int(_) for _ in input().split()]

A.sort(reverse=True)
B.sort(reverse=True)
if A[0] < B[0]:
    print(-1)
    sys.exit()
cnt = 0
while B:
    ci = bi = 0
    while bi < len(B):
        if ci == len(A):
            break
        if A[ci] >= B[bi]:
            ci += 1
            B.pop(bi)
            bi -= 1
        bi += 1

    cnt += 1

print(cnt)

