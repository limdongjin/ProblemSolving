import sys

def main():
    N = int(input())
    T = [0]*(N+1)
    P = [0]*(N+1)
    dp = [-1]*(N+1)

    for day in range(1, N+1):
        T[day], P[day] = map(int, input().split())
    ans = 0
    def go(day):
        if day == N + 1:
            return 0
        if day > N + 1:
            return -sys.maxsize
        if dp[day] != -1:
            return dp[day]

        dp[day] = max(go(day+1) , go(day+T[day])+P[day])
        return dp[day]
    print(go(day=1))


main()
