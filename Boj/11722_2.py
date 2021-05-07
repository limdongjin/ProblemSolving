import sys
input = sys.stdin.readline
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # D[i] : A[i] 로 시작하는 가장 긴 감소 부분수열 길이     
    D = [1]*n
    
    for i in range(n-1, -1, -1):
        m = 0
        for j in range(i+1, n):
            if A[i] > A[j] and m < D[j]:
                m = D[j]

        D[i] += m

    print(max(D))

main()
