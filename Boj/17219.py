import sys

input = sys.stdin.readline

def main():
    n, m = [int(_) for _ in input().split()]
    dic = {}
    for _ in range(n):
        site, pw = input().split()
        dic[site] = pw

    for _ in range(m):
        s = input().rstrip()

        print(dic[s])

main()