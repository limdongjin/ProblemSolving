import sys
input = sys.stdin.readline


def main():
    tc: int = int(input())
    for _ in range(tc):
        n = int(input())
        b = [int(v) for v in input().split()]
        s = sum(b)
        if n == s:
            print(0)
        elif s > n:
            print(s-n)
        else:
            print(1)


main()