import sys
input = sys.stdin.readline

_, A = input(), list(map(int, input().split()))
print(max(A) - min(A))
