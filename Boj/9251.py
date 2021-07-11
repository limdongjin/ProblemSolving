from itertools import product
import sys
input = sys.stdin.readline

def solve(s1, s2):
    # dp[i][j]
    # i : s1 idx, j: s2 idx
    # dp[-1][x] or dp[x][-1] is always 0. 

    N, M = len(s1), len(s2)
    dp = [[0]*(M+1) for _ in range(N+1)]
    
    for i, j in product(range(0,N), range(0,M)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1]+1
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[N-1][M-1]

s1, s2 = input().rstrip(), input().rstrip()
print(solve(s1, s2))
