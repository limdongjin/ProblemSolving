


def main():
    n = int(input())
    # dp[i][j]
    # 1 <= i <= n
    # 0 <= j <= 9

    # dp[i][j] = sum(dp[i-1][k] for k <= j)
    dp = [[1]*10 for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(0, 10):
            dp[i][j] = sum(dp[i-1][:j+1])%10007

    print(sum(dp[n])%10007)
    


main()
