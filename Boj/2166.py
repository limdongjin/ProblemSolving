import math

def solve(p):
    ret = 0
    for i in range(len(p)-1):
        ret += p[i][0]*p[i+1][1] - p[i][1]*p[i+1][0]
    ret = math.fabs(0.5*abs(ret))
    return round(ret, 1)

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append([x, y])
P.append(P[0][:])

print(solve(P))
