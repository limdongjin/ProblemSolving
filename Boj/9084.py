import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1
    # dp[k] : k 를 만드는 경우의 수 
    
    for i in range(N):
        for j in range(A[i], M+1):
            dp[j] += dp[j-A[i]]

    print(dp[M])
