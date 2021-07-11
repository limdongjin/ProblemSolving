import sys
input = sys.stdin.readline

def solve(A, N):
    prev_max_dp = list(next(A))
    prev_min_dp = prev_max_dp[:]

    for line in range(1, N):
        cur_max_dp = list(next(A))
        cur_min_dp = cur_max_dp[:]

        cur_max_dp[0] += max(prev_max_dp[:2])
        cur_max_dp[1] += max(prev_max_dp)
        cur_max_dp[2] += max(prev_max_dp[1:])

        cur_min_dp[0] += min(prev_min_dp[:2])
        cur_min_dp[1] += min(prev_min_dp)
        cur_min_dp[2] += min(prev_min_dp[1:])

        prev_max_dp, prev_min_dp = cur_max_dp, cur_min_dp

    return max(prev_max_dp), min(prev_min_dp)


N = int(input())
A = (map(int, input().split()) for line in range(N))

max_v, min_v = solve(A, N)

print(max_v, min_v)

