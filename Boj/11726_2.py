
dp = {}
def main():
    n = int(input())
    dp[1] = 1
    dp[2] = 2
    print(go(n))
def go(x):
    if x <= 0:
        return 0
    if x in dp:
        return dp[x]

    dp[x] = go(x-1) + go(x-2)
    return dp[x]
main()
