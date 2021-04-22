import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def main():
    a, b = [int(_) for _ in input().split()]
    g = gcd(a, b)
    lcm = g * (a//g) * (b//g)
    print(g)
    print(lcm)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

main()