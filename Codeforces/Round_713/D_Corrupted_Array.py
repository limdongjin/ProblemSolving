import sys
from collections import Counter
input = sys.stdin.readline

def print_l(l):
    ll = [str(_) for _ in l]
    print(' '.join(ll))

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())

        # n + 2
        b = [int(_) for _ in input().split()]
        b.sort()
        nsum = sum(b[:n]) # b1 + b2 + ... bn

        # case1. b1+b2+...bn is (bn or bn+1)
        if b[n] == nsum or b[n+1] == nsum:
            print_l(b[:n])
            continue

        counts = Counter(b[:n+1])
        nsump = nsum + b[n]
        x = nsump - b[n+1]

        # impossible case
        if counts[x] == 0:
            # impossible
            print(-1)
            continue

        ret = []
        xidx = b.index(x)
        for i in range(0, n + 1):
            if i == xidx:
                continue
            ret.append(b[i])
        print_l(ret)


main()