import sys
from copy import deepcopy
input = sys.stdin.readline

def main():
    n = int(input())
    
    # 1 <= level <= N
    # 1 <= col <= level
    # A[level][col]
    A = [[0]*(n+1) for level in range(n+1)]
    for level in range(1, n+1):
        line = list(map(int, input().split()))
        for col, v in enumerate(line):
            A[level][col+1] = v
    

    # D[level][col]=max(D[level-1][col-1],D[level-1][col])+A[level][col]
    # (level, col) 까지 도착했을때 최대합 
    # 초기값: A[level][col]
    D = deepcopy(A)

    for level in range(2, n+1):
        for col in range(1, level+1):
            D[level][col] += max(D[level-1][col-1],
                                D[level-1][col])
    
    print(max(D[n]))

main()
