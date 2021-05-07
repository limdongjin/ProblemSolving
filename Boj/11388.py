import sys
input = sys.stdin.readline
def main():
    n = int(input())
    A = [int(_) for _ in input().split()]
    # D[i] : A[i] 에서 끝나는 최대 연속합
    D = A[:]
    
    # D2[i] : A[i] 에서 시작하는 최대 연속합 
    D2 = A[:]
    
    for i in range(1, n):
        D[i] = max(D[i-1]+A[i], A[i])
    for i in range(n-2, -1, -1):
        D2[i] = max(D2[i+1]+A[i], A[i])

    print(max([D[i-1]+D2[i+1] 
                for i in range(1, n-1)]+[max(D)]))
main()
