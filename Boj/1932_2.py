import sys
input = sys.stdin.readline

def main():
    n = int(input())
    
    # A[level][column]
    A = [[-1]*n for level in range(n)]
    
    # D[level][column]
    # (level, column) 까지 도착했을때 최대합 
    D = A[:]

    for level in range(n):
        line = list(map(int, input().split()))
        for col, v in enumerate(line):
            A[level][col] = v
    D[0][0] = A[0][0]

    for level in range(1, n):
        D[level][0] = D[level-1][0]+A[level][0]
        D[level][level] = D[level-1][level-1]+A[level][level]
        for col in range(1, level):
            # 점화식
            D[level][col] = max(D[level-1][col-1],
                                D[level-1][col]) \
                            + A[level][col]
    
    print(max(D[n-1]))

main()
