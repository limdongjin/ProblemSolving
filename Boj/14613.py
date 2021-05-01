import sys
dp = {}

def main():
    global dp
    n = int(input())
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = min(dp[i-1], dp[i//2]+i%2, dp[i//3]+i%3) + 1
    print(dp[n])

main()
