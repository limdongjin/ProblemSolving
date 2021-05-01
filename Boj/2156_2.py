

def main():
    n = int(input())
    # podo[n]
    podo = []
    
    
    for _ in range(n):
        podo.append(int(input()))
    if n < 3:
        print(sum(podo))
        return
    # dp[n]
    dp = [-1]*n
    dp[0] = podo[0]
    dp[1] = podo[0]+podo[1]
    dp[2] = max(podo[1]+podo[2],
                podo[0]+podo[2],
                dp[1])
    
    def go(idx):
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = max(podo[idx]+podo[idx-1]+go(idx-3),
                      podo[idx]+go(idx-2),
                      go(idx-1))
        return dp[idx]
    
    print(go(n-1))

main()
