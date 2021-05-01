import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def main():
    N = int(input())

    # dp[N+1][10] 
    # dp[leng][idx]
    dp = [[0 for _ in range(10)] for _ in range(N+5)]
    for idx in range(1, 10):
        dp[1][idx] = 1
    
    ret = 0
    for idx in range(10):
        ret += go(idx, N, dp)
    print(ret % 1000000000)

def go(idx, leng, dp):
    if leng < 1 or idx < 0 or idx > 9 or (idx == 0 and leng == 1):
        return 0
    if dp[leng][idx] != 0:
        return dp[leng][idx]
    
    dp[leng][idx] = go(idx-1, leng-1, dp) + go(idx+1, leng-1, dp)
    return dp[leng][idx]

main()
