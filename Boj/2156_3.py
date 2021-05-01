import sys
input = sys.stdin.readline

def main():
    n = int(input())
    
    podo = [0]*n
    for i in range(n):
        podo[i] = int(input())
    if n < 3:
        print(sum(podo))
        return

    dp = [-1]*n
    dp[0] = podo[0]
    dp[1] = podo[0] + podo[1]
    dp[2] = max(podo[2]+podo[1],
                podo[2]+podo[0],
                dp[1])
    for i in range(3, n):
        dp[i] = max(podo[i]+podo[i-1]+dp[i-3],
                    podo[i]+dp[i-2],
                    dp[i-1])
    print(dp[n-1])
main()
