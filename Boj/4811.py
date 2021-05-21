import sys
input=sys.stdin.readline

MAX_N = 30

# dp[W][H] : (w, h) 조합에서 문자열 경우의 수
# w: 한조각짜리 개수, h: 반조각 짜리 개수 
dp = [[1]*(MAX_N+1) for _ in range(MAX_N+1)]

for w in range(1, MAX_N+1):
    dp[w][0] = dp[w-1][1]
    for h in range(1, MAX_N-w+1):
        dp[w][h] = dp[w][h-1] + dp[w-1][h+1]

while True:
    n = int(input())
    if n == 0:
        break 
    
    print(dp[n][0])
