import sys
input = sys.stdin.readline

def solve(a):
    l = 0
    r = len(a)-1
    min_ij = (a[0], a[1])
    min_v = abs(sum(min_ij))

    while l < r and min_v:
        v = a[l] + a[r]
        if abs(v) < min_v:
            min_v = abs(v)
            min_ij = (a[l], a[r])
        if v < 0:
            l += 1
        else:
            r -= 1

    print(min_ij[0], min_ij[1])
input()
A = sorted([int(_) for _ in input().split()])

solve(A)
