import sys
input = sys.stdin.readline
def main():
    n = int(input())
    dp = [sys.maxsize]*(n+5)    
    dp[1] = 0
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = min(dp[i//3]+i%3,
                    dp[i//2]+i%2,
                    dp[i-1]) + 1
    print(dp[n])

main()
