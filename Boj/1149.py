from enum import Enum
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

class Color(Enum):
    R = 0
    G = 1
    B = 2

def go(i, color, costs, dp):
    if dp[i][color] != -1:
        return dp[i][color]
    other1, other2 = [v.value for v in Color if v.value != color]
    dp[i][color] = min(go(i-1, other1, costs, dp), go(i-1, other2, costs, dp)) + costs[i][color]
    return dp[i][color]

def main():
    N = int(input())
    
    # costs[N+1][3]
    costs = [[-1, -1, -1] for _ in range(N+1)]
    dp = [[-1, -1, -1] for _ in range(N+1)]
    R, G, B = map(lambda x: x.value, Color)
    
    for i in range(1, N+1):
        costs[i][R], costs[i][G], costs[i][B] = map(int, input().split())
    dp[1][R], dp[1][G], dp[1][B] = costs[1][R], costs[1][G], costs[1][B]

    ret = min(go(N, R, costs, dp), go(N, G, costs, dp), go(N, B, costs, dp))
    print(ret)


main()
