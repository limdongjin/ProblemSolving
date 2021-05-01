

def main():
    n = int(input())
    # dp[N+1][3]
    # dp = [ [0]*3 for _ in range(n+1)]
    # dp[1][0] = 1
    # dp[1][1] = 1
    # dp[1][2] = 1
    prev0, prev1, prev2 = 1, 1, 1
    for i in range(2, n+1):
        cur0 = (prev0 + prev1 + prev2)%9901
        cur1 = (prev0 + prev2)%9901
        cur2 = (prev0 + prev1)%9901
        prev0, prev1, prev2 = cur0, cur1, cur2

        #dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        #dp[i][1] = dp[i-1][0] + dp[i-1][2]
        #dp[i][2] = dp[i-1][0] + dp[i-1][1]
    
    # dp[n][0] + dp[n][1] + dp[n[2]
    print((prev0+prev1+prev2)%9901)

main()
