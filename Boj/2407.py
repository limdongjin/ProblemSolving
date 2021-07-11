import sys
input=sys.stdin.readline

def ncm(n, m):
    if n == m or m == 0:
        return 1
    if dp[n][m] != -1:
        return dp[n][m]
    
    dp[n][m] = ncm(n-1, m-1) + ncm(n-1, m)
    return dp[n][m]
    

N, M = map(int, input().split())

# dp[n][m]
dp = [[-1]*(M+1) for _ in range(N+1)]
print(ncm(N, M))
