

N, M = map(int, input().split())
A = [[0]*(M+1) for _ in range(N+1)]

# DP[y][x] : (y, x) 까지 왔을때 가장 큰 정사각형 한변 길이  
# DP[y][x] = min(DP[y-1][x], DP[y][x-1], DP[y-1][x-1]) + 1
DP = [[0]*(M+1) for _ in range(N+1)]
 

for y in range(1, N+1):
    for idx, v in enumerate(list(map(int, input()))):
        A[y][idx+1] = v

for y in range(1, N+1):
    for x in range(1, M+1):
        if not A[y][x]:
            continue
        DP[y][x] = min(DP[y-1][x], DP[y][x-1], DP[y-1][x-1]) + 1

print(max(max(row) for row in DP) ** 2)
