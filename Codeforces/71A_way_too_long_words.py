import sys
input = sys.stdin.readline

def main():
    n = int(input())

    for _ in range(n):
        s = input().rstrip()
        if len(s) <= 10:
            print(s)
            continue

        print(s[0] + str(len(s) - 2) + s[-1])

main()