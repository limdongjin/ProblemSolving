import sys
input = sys.stdin.readline


def main():
    n = int(input())
    dp = [10**6+1]*(n+2)
    rev_dp = [10**6+1]*(n+2)

    dp[1] = 0
    rev_dp[1] = 0

    dp[2] = 1
    rev_dp[2] = 1

    for i in range(3, n+1):
        tmp = dp[i//3] + i % 3
        rev_dp[i] = i // 3

        if dp[i//2] + i % 2 <= tmp:
            tmp = dp[i//2] + i % 2
            rev_dp[i] = i // 2

        if dp[i-1] <= tmp:
            tmp = dp[i-1]
            rev_dp[i] = i-1

        dp[i] = tmp + 1

    i = n
    hist = []
    while i != 0:
        hist.append(i)
        i = rev_dp[i]

    print(dp[n])
    print(" ".join(map(str, hist)))


main()