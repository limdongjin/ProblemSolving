

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
for f in range(N):
    for s in range(f+1, N):
        for t in range(s+1, N):
            tmp = A[f] + A[s] + A[t]
            if tmp <= M:
                ans = max(tmp, ans)

print(ans)
