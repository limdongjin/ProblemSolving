import sys
input = sys.stdin.readline

N, B = int(input()), list(map(int, input().split()))
A = [B[0]] + [(i+1)*B[i] - i*B[i-1] for i in range(1, N)]

print(' '.join(map(str, A)))
