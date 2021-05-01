import sys
input = sys.stdin.readline
def main():
    n = int(input())
    
    # A[n] 
    A = list(map(int, input().split()))
    
    # D[n]
    # D[i] : i 번째 요소로 끝나는 부분수열의 최대합
    D = A[:]

    for i in range(n):
        m = 0
        for j in range(i):
            if A[j] < A[i] and m < D[j]:
                m = D[j]
        
        D[i] += m
    
    print(max(D))
main()
