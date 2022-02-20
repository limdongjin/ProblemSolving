from sys import stdin
input = stdin.readline


def solve(n, k, seq):
    ret = odd = left = 0

    for right in range(n):
        if seq[right] % 2: odd += 1
        while odd > k: # left-pointer move
            if seq[left] % 2: odd -= 1
            left += 1
        ret = max(ret, right-left-odd+1)
    return ret


def main():
    N, K = map(int, input().split())
    S = [int(_) for _ in input().split()]

    print(solve(N, K, S))

main()