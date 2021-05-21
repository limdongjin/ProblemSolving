import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
MAX_A = 1000000000

# 1 <= i <= N
A = [0]+[int(input()) for _ in range(N)]

# dp[i] : i 번째 오렌지까지 포장했을때 최소 비용
dp = [0]*(N+1)
dp[1] = K

for i in range(2, N+1):
    min_v = max_v = A[i]
    
    dp[i] = dp[i-1]+K
    for siz in range(2, min(M, i)+1):
        # j: 포장하는 box 의 가장 왼쪽 오렌지 
        j = i - siz + 1 

        min_v, max_v = min(min_v, A[j]), max(max_v, A[j])
        
        box_cost = K+siz*(max_v-min_v)
        
        dp[i] = min(dp[i], dp[j-1]+box_cost)

print(dp[N])
