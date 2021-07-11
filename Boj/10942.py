import sys
input = sys.stdin.readline

def make_ans(a, n):
    # dp[start][end]
    # 1 : is palindrome
    # 0 : is not palindrome
    dp = [[0]*(n+1) for _ in range(n+1)]

    # size 1
    for i in range(n):
        dp[i][i] = 1

    # size 2
    for i in range(n-1):
        if A[i] == A[i+1]:
            dp[i][i+1] = 1

    for size in range(3, n+1):
        for start in range(0, n-size+1):
            end = start+size-1
            if A[start] == A[end] and dp[start+1][end-1]:
                dp[start][end] = 1
    return dp

N = int(input())
A = [int(_) for _ in input().split()]
M = int(input())

ans = make_ans(A, N)
for _ in range(M):
    start, end = map(int, input().split())
    print(ans[start-1][end-1])
