import sys
input = sys.stdin.readline

def main():
    n, m, a = [int(_) for _ in input().split()]

    y = n // a + 1 if n % a else n // a
    x = m // a + 1 if m % a else m // a

    print(y*x)

main()