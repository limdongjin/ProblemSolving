import sys

N = int(input())
if N%2 == 1:
    print(0)
    sys.exit()

dp = [0]*(31)
dp[2] = 3
dp[4] = 11

for k in range(6, N+1):
    dp[k] = dp[2]*dp[k-2]
    dp[k] += sum(2*dp[k-i] for i in range(4, k-1, 2))
    dp[k] += 2
print(dp[N])
