from collections import deque

def solve(h):
    n = len(h)
    h.append(0)
    remaining = deque()
    ret = 0

    for i in range(len(h)):
        while remaining and h[remaining[-1]] >= h[i]:
            j = remaining.pop()
            width = i if not remaining else i-remaining[-1]-1
            ret = max(ret, h[j]*width)
        remaining.append(i)
    return ret
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(A))
