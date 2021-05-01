import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
def main():
    N = int(input())
    # podo[N]
    podo = [-1 for _ in range(N)]
    dp = podo[:]

    for i in range(N):
        v = int(input())
        podo[i] = v
    if N < 3:
        print(sum(podo))
        sys.exit(0)
    dp[0] = podo[0]
    dp[1] = podo[0]+podo[1]
    dp[2] = max(podo[0]+podo[2], podo[2]+podo[1])

    print(go(N-1, podo, dp))

def go(idx, podo, dp):
    if idx < 0:
        assert False
    if dp[idx] != -1:
        return dp[idx]
    go(idx-1, podo, dp)
    go(idx-2, podo, dp)
    go(idx-3, podo, dp)
    dp[idx] = max(podo[idx-1] + dp[idx-3] + podo[idx], dp[idx-2] + podo[idx], dp[idx - 1])
    return dp[idx]


main()
