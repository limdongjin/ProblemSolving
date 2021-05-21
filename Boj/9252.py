

def solve(s1, s2):
    n1, n2 = len(s1), len(s2)
    s1 = " "+s1
    s2 = " "+s2

    # dp[n1+1][n2+1]
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    
    # dp table setup
    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            if s1[i1] == s2[i2]:
                dp[i1][i2] = dp[i1-1][i2-1] + 1
            else:
                dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
    print(dp[n1][n2])
    
    ans = ''
    i1, i2 = n1, n2
    while dp[i1][i2]:
        if s1[i1] == s2[i2]:
            ans += s1[i1]
            i1, i2 = i1-1, i2-1
        elif dp[i1][i2] == dp[i1-1][i2]:
            i1 -= 1
        else:
            i2 -= 1
    print(ans[::-1])
A = input().rstrip()
B = input().rstrip()

solve(A, B)
