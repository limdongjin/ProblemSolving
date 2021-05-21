import sys
input = sys.stdin.readline

# dp[1][i] = 1
# dp[n][0] = sum(dp[n-1])
# dp[n][i] = sum(dp[n][i-1] - dp[n-1][i-1])
dp = [[1]*10 for _ in range(66)]

for nn in range(2, 66):
    dp[nn][0] = sum(dp[nn-1])
    for i in range(1, 10):
        dp[nn][i] = dp[nn][i-1] - dp[nn-1][i-1]

for _ in range(int(input())):
    n = int(input())
    print(dp[n+1][0])