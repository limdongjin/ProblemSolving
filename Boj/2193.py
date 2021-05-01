

def main():
    n = int(input())
    pprev, prev = 0, 1
    # equivalance: dp[0] = 0, dp[1] = 1
    # pprev : dp[n-2] 
    # prev : dp[n-1]

    ret = 0
    for i in range(2, n+1):
        # dp[n] = dp[n-1] + dp[n-2]
        pprev, prev = prev, pprev + prev
    print(prev)
    

main()
