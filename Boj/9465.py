import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(3)]
    # dp[way][i] 

    dp[0][0] = A[0][0]
    dp[1][0] = A[1][0]
    dp[2][0] = 0

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + A[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + A[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

    print(max(dp[way][n-1] for way in range(3)))
    
    
