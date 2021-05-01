import sys


def main():
    N = int(input())
    A = [int(_) for _ in input().split()]
    
    # dp[N]
    dp = [0]*N
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if A[j] < A[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    print(max(dp))

main()
