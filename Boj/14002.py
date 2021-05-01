

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0]*N
    v = [-1]*N

    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if A[j] < A[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                v[i] = j
    max_v = 0
    max_i = 0
    for i in range(N):
        if max_v < dp[i]:
            max_v = dp[i]
            max_i = i

    print(max_v)
    def get_trace():
        ret = []
        x = max_i
        while x != -1:
            ret.append(A[x])
            x = v[x]
        return ret

    ret = get_trace()
    print(' '.join(map(str,ret[::-1])))

main()
