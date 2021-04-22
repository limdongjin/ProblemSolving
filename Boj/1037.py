import sys
input = sys.stdin.readline

def main():
    input()
    a = [int(_) for _ in input().split()]
    a.sort()
    print(a[0]*a[-1])

main()