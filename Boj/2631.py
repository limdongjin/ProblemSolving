import sys
input=sys.stdin.readline

def solve(a):
    # n - (A 의 가장 긴증가 부분 수열 길이) 

    n = len(A)
    
    # d[i] : i 로 시작하는 가장 긴 증가 부분 수열
    # 초기값 : 1 
    d =[1 for _ in range(n)]
    
    for i in range(n-2, -1, -1):
        d[i] = max([d[j] for j in range(i+1, n) if a[i] < a[j]], default=0) + 1
    
    return n - max(d)

N, A= int(input()), [int(input()) for _ in range(N)]
print(solve(A))
