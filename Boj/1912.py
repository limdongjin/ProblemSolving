import sys
sys.setrecursionlimit(100001)
def main():
    n = int(input())
    A = list(map(int, input().split()))
    dp = [-sys.maxsize]*n
    dp[0] = A[0]
    go(n-1, A, dp)

    print(max(dp))
def go(i, A, dp):
    if dp[i] != -sys.maxsize:
        return dp[i]
    dp[i] = max(go(i-1, A, dp) + A[i], A[i])
    return dp[i]
main()
