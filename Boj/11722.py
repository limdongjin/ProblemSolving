import sys
input = sys.stdin.readline

def main():
    n = int(input())
    A = [int(_) for _ in input().split()]
    D = [1 for _ in range(n)]
    
    for i in range(n):
        m = 0
        for j in range(i):
            if A[j] > A[i] and m < D[j]:
                m = D[j]
        D[i] += m

    print(max(D))

main()
